import cv2
import time
import boto3
import os
import dotenv
import threading
# import RPi.GPIO as gpio

dotenv.load_dotenv()

REFERENCE = os.environ.get('REFERENCE_IMAGE')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.environ.get('BUCKET_NAME')

if not os.path.exists('rostos'):
    os.makedirs('rostos')


# # Configure pinnout
# def config_pin(PIN=3):
#     print("Configuring pin...")
#     gpio.setmode(gpio.BCM)
#     gpio.setup(PIN, gpio.OUT)
#     gpio.output(PIN, gpio.LOW)

# # Functions
# def send_to_pico(PIN=3):
#     print("Sending signal to Pico...")
#     gpio.output(PIN, gpio.HIGH)
#     time.sleep(1)
#     gpio.output(PIN, gpio.LOW)

# AWS Functions
def upload_to_s3(client, file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_path

    try:
        response = client.upload_file(file_path, bucket_name, object_name)
    except Exception as e:
        print(f"Failed to upload to S3: {e}")
        return False
    return True


def compare_faces(client, bucket, ref_image, target_image):
    try:
        response = client.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': ref_image,
                }
            },
            TargetImage={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': target_image,
                }
            },
            SimilarityThreshold=70
        )
        return response
    except Exception as e:
        print(f"Failed to compare faces: {e}")
        return None

# OpenCV Functions
def draw_rectangle(frame, x, y, w, h):
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

def face_detection(client_s3, client_rekognition, bucket_name, cap):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    last_time = time.time()

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            draw_rectangle(frame, x, y, w, h)

        current_time = time.time()
        if current_time - last_time >= 5 and len(faces) > 0:
            last_time = time.time()
            filename = f"rostos/face_detected_{int(current_time)}.jpg"
            print("5 seconds have passed and face detected")
            cv2.imwrite(filename, frame)

            cv2.imshow('Camera Feed', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            object_name = filename

            if upload_to_s3(client_s3, filename, bucket_name, object_name):
                print(f'File {filename} uploaded to {bucket_name} as {object_name}')
            else:
                print(f'File {filename} could not be uploaded to {bucket_name} as {object_name}')

            response = compare_faces(client_rekognition, bucket_name, REFERENCE, object_name)

            if not response:
                continue

            if not response.get('FaceMatches'):
                similarity = 0
            else:
                similarity = response['FaceMatches'][0]['Similarity']

            if similarity >= 70:
                print('It is him')
                print('Sending signal to Pico...')
                # send_to_pico()
            else:
                print('It is not him')

        time.sleep(0.1)


# def show_camera_feed(cap):

#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#     while True:
#         ret, frame = cap.read()
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#         for (x, y, w, h) in faces:
#             draw_rectangle(frame, x, y, w, h)

#         if not ret:
#             print("Failed to capture frame")
#             break

#         cv2.imshow('Camera Feed', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break


# Main
if __name__ == '__main__':

    # config_pin()
    
    try:
        print("Press ctrl+c to stop the program")
        print("Starting camera feed...")
        client_s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        client_rekognition = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

        cap = cv2.VideoCapture(0)

        # camera_thread = threading.Thread(target=show_camera_feed, args=(cap,))
        # camera_thread.daemon = True
        # camera_thread.start()

        face_detection(client_s3, client_rekognition, BUCKET_NAME, cap)

    except KeyboardInterrupt:
        print("Program stopped")
        print("Press q while on the camera feed window to stop the camera feed")
        # camera_thread.join()
        cap.release()
        cv2.destroyAllWindows()
        print("Camera feed stopped")
        print("Program ended")
