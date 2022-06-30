import pandas as pd

def cut_csv(total_data_number, frame_count, df):

    for i in range(total_data_number):
        if float(df.at[df.index[i], "R+G+B Value"]) < 8:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\07.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 16 and float(df.at[df.index[i], "R+G+B Value"]) >= 8:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\815.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 24 and float(df.at[df.index[i], "R+G+B Value"]) >= 16:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\1623.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 32 and float(df.at[df.index[i], "R+G+B Value"]) >= 24:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\2431.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 40 and float(df.at[df.index[i], "R+G+B Value"]) >= 32:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\3239.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 48 and float(df.at[df.index[i], "R+G+B Value"]) >= 40:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\4047.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 56 and float(df.at[df.index[i], "R+G+B Value"]) >= 48:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\4855.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 64 and float(df.at[df.index[i], "R+G+B Value"]) >= 56:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\5663.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 72 and float(df.at[df.index[i], "R+G+B Value"]) >= 64:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\6471.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 80 and float(df.at[df.index[i], "R+G+B Value"]) >= 72:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\7279.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 88 and float(df.at[df.index[i], "R+G+B Value"]) >= 80:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\8087.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 96 and float(df.at[df.index[i], "R+G+B Value"]) >= 88:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\8895.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 104 and float(df.at[df.index[i], "R+G+B Value"]) >= 96:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\96103.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 112 and float(df.at[df.index[i], "R+G+B Value"]) >= 104:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\104111.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 120 and float(df.at[df.index[i], "R+G+B Value"]) >= 112:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\112119.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 128 and float(df.at[df.index[i], "R+G+B Value"]) >= 120:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\120127.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 136 and float(df.at[df.index[i], "R+G+B Value"]) >= 128:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\128135.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 144 and float(df.at[df.index[i], "R+G+B Value"]) >= 136:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\136143.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 152 and float(df.at[df.index[i], "R+G+B Value"]) >= 144:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\144151.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 160 and float(df.at[df.index[i], "R+G+B Value"]) >= 152:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\152159.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 168 and float(df.at[df.index[i], "R+G+B Value"]) >= 160:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\160167.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 176 and float(df.at[df.index[i], "R+G+B Value"]) >= 168:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\168175.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 184 and float(df.at[df.index[i], "R+G+B Value"]) >= 176:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\176183.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 192 and float(df.at[df.index[i], "R+G+B Value"]) >= 184:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\184191.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 200 and float(df.at[df.index[i], "R+G+B Value"]) >= 192:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\192199.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 208 and float(df.at[df.index[i], "R+G+B Value"]) >= 200:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\200207.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 216 and float(df.at[df.index[i], "R+G+B Value"]) >= 208:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\208215.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 224 and float(df.at[df.index[i], "R+G+B Value"]) >= 216:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\216223.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 232 and float(df.at[df.index[i], "R+G+B Value"]) >= 224:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\224231.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 240 and float(df.at[df.index[i], "R+G+B Value"]) >= 232:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\232239.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 248 and float(df.at[df.index[i], "R+G+B Value"]) >= 240:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\240247.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 256 and float(df.at[df.index[i], "R+G+B Value"]) >= 248:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\248255.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 264 and float(df.at[df.index[i], "R+G+B Value"]) >= 256:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\256263.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 272 and float(df.at[df.index[i], "R+G+B Value"]) >= 264:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\264271.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 280 and float(df.at[df.index[i], "R+G+B Value"]) >= 272:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\272279.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 288 and float(df.at[df.index[i], "R+G+B Value"]) >= 280:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\280287.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 296 and float(df.at[df.index[i], "R+G+B Value"]) >= 288:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\288295.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 304 and float(df.at[df.index[i], "R+G+B Value"]) >= 296:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\296303.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 312 and float(df.at[df.index[i], "R+G+B Value"]) >= 304:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\304311.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 320 and float(df.at[df.index[i], "R+G+B Value"]) >= 312:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\312319.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 328 and float(df.at[df.index[i], "R+G+B Value"]) >= 320:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\320327.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 336 and float(df.at[df.index[i], "R+G+B Value"]) >= 328:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\328335.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 344 and float(df.at[df.index[i], "R+G+B Value"]) >= 336:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\336343.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 352 and float(df.at[df.index[i], "R+G+B Value"]) >= 344:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\344351.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 360 and float(df.at[df.index[i], "R+G+B Value"]) >= 352:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\352359.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 368 and float(df.at[df.index[i], "R+G+B Value"]) >= 360:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\360367.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 376 and float(df.at[df.index[i], "R+G+B Value"]) >= 368:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\368375.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 384 and float(df.at[df.index[i], "R+G+B Value"]) >= 376:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\376383.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 392 and float(df.at[df.index[i], "R+G+B Value"]) >= 384:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\384391.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 400 and float(df.at[df.index[i], "R+G+B Value"]) >= 392:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\392399.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 408 and float(df.at[df.index[i], "R+G+B Value"]) >= 400:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\400407.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 416 and float(df.at[df.index[i], "R+G+B Value"]) >= 408:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\408415.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 424 and float(df.at[df.index[i], "R+G+B Value"]) >= 416:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\416423.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 432 and float(df.at[df.index[i], "R+G+B Value"]) >= 424:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\424431.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 440 and float(df.at[df.index[i], "R+G+B Value"]) >= 432:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\432439.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 448 and float(df.at[df.index[i], "R+G+B Value"]) >= 440:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\440447.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 456 and float(df.at[df.index[i], "R+G+B Value"]) >= 448:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\448455.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 464 and float(df.at[df.index[i], "R+G+B Value"]) >= 456:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\456463.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 472 and float(df.at[df.index[i], "R+G+B Value"]) >= 464:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\464471.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 480 and float(df.at[df.index[i], "R+G+B Value"]) >= 472:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\472479.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 488 and float(df.at[df.index[i], "R+G+B Value"]) >= 480:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\480487.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 496 and float(df.at[df.index[i], "R+G+B Value"]) >= 488:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\488495.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 504 and float(df.at[df.index[i], "R+G+B Value"]) >= 496:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\496503.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 512 and float(df.at[df.index[i], "R+G+B Value"]) >= 504:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\504511.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 520 and float(df.at[df.index[i], "R+G+B Value"]) >= 512:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\512519.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 528 and float(df.at[df.index[i], "R+G+B Value"]) >= 520:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\520527.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 536 and float(df.at[df.index[i], "R+G+B Value"]) >= 528:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\528535.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 544 and float(df.at[df.index[i], "R+G+B Value"]) >= 536:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\536543.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 552 and float(df.at[df.index[i], "R+G+B Value"]) >= 544:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\544551.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 560 and float(df.at[df.index[i], "R+G+B Value"]) >= 552:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\552559.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 568 and float(df.at[df.index[i], "R+G+B Value"]) >= 560:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\560567.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 576 and float(df.at[df.index[i], "R+G+B Value"]) >= 568:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\568575.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 584 and float(df.at[df.index[i], "R+G+B Value"]) >= 576:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\576583.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 592 and float(df.at[df.index[i], "R+G+B Value"]) >= 584:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\584591.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 600 and float(df.at[df.index[i], "R+G+B Value"]) >= 592:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\592599.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 608 and float(df.at[df.index[i], "R+G+B Value"]) >= 600:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\600607.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 616 and float(df.at[df.index[i], "R+G+B Value"]) >= 608:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\608615.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 624 and float(df.at[df.index[i], "R+G+B Value"]) >= 616:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\616623.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 632 and float(df.at[df.index[i], "R+G+B Value"]) >= 624:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\624631.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 640 and float(df.at[df.index[i], "R+G+B Value"]) >= 632:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\632639.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 648 and float(df.at[df.index[i], "R+G+B Value"]) >= 640:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\640647.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 656 and float(df.at[df.index[i], "R+G+B Value"]) >= 648:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\648655.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 664 and float(df.at[df.index[i], "R+G+B Value"]) >= 656:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\656663.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 672 and float(df.at[df.index[i], "R+G+B Value"]) >= 664:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\664671.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 680 and float(df.at[df.index[i], "R+G+B Value"]) >= 672:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\672679.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 688 and float(df.at[df.index[i], "R+G+B Value"]) >= 680:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\680687.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 696 and float(df.at[df.index[i], "R+G+B Value"]) >= 688:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\688695.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 704 and float(df.at[df.index[i], "R+G+B Value"]) >= 696:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\696703.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 712 and float(df.at[df.index[i], "R+G+B Value"]) >= 704:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\704711.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 720 and float(df.at[df.index[i], "R+G+B Value"]) >= 712:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\712719.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 728 and float(df.at[df.index[i], "R+G+B Value"]) >= 720:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\720727.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 736 and float(df.at[df.index[i], "R+G+B Value"]) >= 728:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\728735.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 744 and float(df.at[df.index[i], "R+G+B Value"]) >= 736:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\736743.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 752 and float(df.at[df.index[i], "R+G+B Value"]) >= 744:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\744751.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 760 and float(df.at[df.index[i], "R+G+B Value"]) >= 752:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\752759.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
        elif float(df.at[df.index[i], "R+G+B Value"]) < 768 and float(df.at[df.index[i], "R+G+B Value"]) >= 760:
            f = open("\\\\C:\\Users\\italab\\Desktop\\study_program\\Study_program\\csv_result\\hino\\frame" + str(frame_count) + "\\760767.csv", "a")
            f.write([float(df.at[df.index[i], "R Value"]), float(df.at[df.index[i], "G Value"]), float(df.at[df.index[i], "B Value"]), float(df.at[df.index[i], "R+G+B Value"]), float(df.at[df.index[i], "R-B Value"])])
            f.close()
