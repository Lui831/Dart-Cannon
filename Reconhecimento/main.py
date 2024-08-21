import cv2
import time
import boto3
import os
import dotenv

dotenv.load_dotenv()

REFERENCE = os.environ.get('REFERENCE_IMAGE')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME=os.environ.get('BUCKET_NAME')



def upload_to_s3(client, file_path, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_path

    try:
        response = client.upload_file(file_path, bucket_name, object_name)
    except:
        return False
    return True


def compare_faces(client, bucket, ref_image, target_image):
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


if __name__ == '__main__':

    client_s3 = boto3.client('s3', region_name='us-east-1', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    client_rekognition = boto3.client('rekognition', region_name='us-east-1', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    last_time = time.time()

    bucket_name = BUCKET_NAME

    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        cv2.imshow('frame', frame)

        current_time = time.time()
        if current_time - last_time >= 5 and len(faces) > 0:
            last_time = time.time()
            filename = f"rostos/face_detected_{int(current_time)}.jpg"
            print("5 second has passed and face detected")
            cv2.imwrite(filename, frame)

            object_name = filename

            if upload_to_s3(client_s3, filename, bucket_name, object_name):
                print(f'File {filename} uploaded to {bucket_name} as {object_name}')
            else:
                print(f'File {filename} could not be uploaded to {bucket_name} as {object_name}')

            response = compare_faces(client_rekognition, bucket_name, REFERENCE, object_name)

            # print(response)

            if not response.get('FaceMatches'):
                similarity = 0
            else:
                similarity = response['FaceMatches'][0]['Similarity']

            if similarity >= 70:
                print('É ele')
            else:
                print('Não é ele')

        if cv2.waitKey(1) == ord('q'):
            break



        


    cap.release()
    cv2.destroyAllWindows()

    


