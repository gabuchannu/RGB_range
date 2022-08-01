import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# Webカメラ入力の場合：
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(".//data_movie//hino_yoko.mp4" )
count = 1
frame_count = 1

with mp_face_mesh.FaceMesh(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    if count == 30: #1秒経過していたら
        count = 1 #カウンターを初期化
        # 後で自分撮りビューを表示するために画像を水平方向に反転し、BGR画像をRGBに変換
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # パフォーマンスを向上させるには、オプションで、参照渡しのためにイメージを書き込み不可としてマーク
        image.flags.writeable = False
        results = face_mesh.process(image)
        
        if results == None:
            print("Can't take face.")
            continue

            # 画像に顔メッシュのアノテーションを描画
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                image=image,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=drawing_spec,
                connection_drawing_spec=drawing_spec)
                cv2.imshow('MediaPipe FaceMesh', image)
                cv2.imwrite(".//data_movie//hino//hino_yoko_" + str(frame_count) + ".png", image)
                frame_count += 1

    else: #countが30未満だったら
        count = count + 1 #countを増やす

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()