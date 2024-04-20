import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('student.db')
cur = conn.cursor()

# 테이블 생성

def create_table():

        conn.execute('create table student (no integer primary key autoincrement, name text)')
        conn.commit()

# 학생 정보 삽입
def insert_student(id, name):
    cur.execute("INSERT INTO students (id, name) VALUES (?, ?)", (id, name))
    conn.commit()

# 출입 확인 함수
def check_access(id):
    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cur.fetchone()
    if student:
        print(f"환영합니다, {student[1]}님!")
    else:
        print("학생 정보를 찾을 수 없습니다. 다시 확인해주시길 바랍니다.")

# 학생 정보 삽입 예시
    insert_student('1101', '곽호영')
    insert_student('1102', '김담휘')
    insert_student('1103', '김민건'),
    insert_student('1104', '김범준'),
    insert_student('1105', '김영균'),
    insert_student('1106', '김영조'),
    insert_student('1107', '김지원'),
    insert_student('1108', '김창규'),
    insert_student('1109', '노윤철'),
    insert_student('1110', '유성재'),
    insert_student('1111', '유승원'),
    insert_student('1112', '유초비'),
    insert_student('1113', '윤상원'),
    insert_student('1114', '이정호'),
    insert_student('1115', '이현우'),
    insert_student('1116', '정우석'),
    insert_student('1117', '정효림'),
    insert_student('1118', '천현서'),
    insert_student('1119', '최하영'),
    insert_student('1120', '홍진기'),
    insert_student('1201', '강승원'),
    insert_student('1202', '권하늬'),
    insert_student('1203', '김윤하'),
    insert_student('1204', '김한중'),
    insert_student('1205', '남규민'),
    insert_student('1206', '민지현'),
    insert_student('1207', '박서진'),
    insert_student('1208', '박재현'),
    insert_student('1209', '박찬웅'),
    insert_student('1210', '서민성'),
    insert_student('1211', '원재인'),
    insert_student('1212', '원하담'),
    insert_student('1213', '이강현'),
    insert_student('1214', '이건희'),
    insert_student('1215', '이민찬'),
    insert_student('1216', '이주섭'),
    insert_student('1217', '이주혁'),
    insert_student('1218', '이지호'),
    insert_student('1219', '임지승'),
    insert_student('1220', '최원섭'),
    insert_student('1221', '홍서현'),
    insert_student('1301', '권민기'),
    insert_student('1302', '김나람'),
    insert_student('1303', '김민준'),
    insert_student('1304', '김소희'),
    insert_student('1305', '김승호'),
    insert_student('1306', '김진후'),
    insert_student('1307', '노아현'),
    insert_student('1308', '박기동'),
    insert_student('1309', '송유찬'),
    insert_student('1310', '심민섭'),
    insert_student('1311', '심예성'),
    insert_student('1312', '이동률'),
    insert_student('1313', '이아림'),
    insert_student('1314', '이원희'),
    insert_student('1315', '임승준'),
    insert_student('1316', '임휘수'),
    insert_student('1317', '정단비'),
    insert_student('1318', '정하민'),
    insert_student('1319', '허강현'),
    insert_student('1320', '허정원'),
    insert_student('2101', '곽민지'),
    insert_student('2102', '구지민'),
    insert_student('2103', '권오찬'),
    insert_student('2104', '김대유'),
    insert_student('2105', '김민건'),
    insert_student('2106', '김민서'),
    insert_student('2107', '김예안'),
    insert_student('2108', '김현서'),
    insert_student('2109', '박상훈'),
    insert_student('2110', '배상훈'),
    insert_student('2111', '서동민'),
    insert_student('2112', '안중근'),
    insert_student('2113', '윤세현'),
    insert_student('2114', '이병민'),
    insert_student('2115', '이신후'),
    insert_student('2116', '이진구'),
    insert_student('2117', '정민규'),
    insert_student('2118', '정준섭'),
    insert_student('2119', '채은우'),
    insert_student('2120', '한경은'),
    insert_student('2202', '강민채'),
    insert_student('2203', '김지호'),
    insert_student('2204', '김현진'),
    insert_student('2205', '박지용'),
    insert_student('2206', '방영민'),
    insert_student('2207', '서은영'),
    insert_student('2208', '이예복'),
    insert_student('2209', '이원준'),
    insert_student('2210', '이종욱'),
    insert_student('2211', '이주영'),
    insert_student('2212', '이혁준'),
    insert_student('2213', '장문경'),
    insert_student('2214', '전한나'),
    insert_student('2215', '정승문'),
    insert_student('2216', '조문기'),
    insert_student('2217', '조성문'),
    insert_student('2218', '최종현'),
    insert_student('2219', '함형진'),
    insert_student('2301', '김긍현'),
    insert_student('2302', '김대현'),
    insert_student('2303', '김령경'),
    insert_student('2304', '김민준'),
    insert_student('2305', '김예은'),
    insert_student('2306', '김태현'),
    insert_student('2307', '노윤석'),
    insert_student('2308', '민지솔'),
    insert_student('2309', '박호건'),
    insert_student('2310', '배준형'),
    insert_student('2311', '우상욱'),
    insert_student('2312', '이상준'),
    insert_student('2313', '이수빈'),
    insert_student('2314', '이예훈'),
    insert_student('2315', '이주헌'),
    insert_student('2316', '임관우'),
    insert_student('2317', '정민'),
    insert_student('2318', '진명준'),
    insert_student('2319', '최지민'),

# 추가적으로 필요한 학생 정보를 여기에 추가할 수 있습니다.

# 출입 확인 예시
student_id = input("학생증의 학번을 입력하세요: ")
check_access(student_id)

# 데이터베이스 연결 종료
conn.close()