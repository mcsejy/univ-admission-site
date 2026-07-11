// 주요 대학 메인 홈페이지 URL
const UNI_MAIN_URL = {
    '서울대학교':     'https://www.snu.ac.kr',
    '연세대학교':     'https://www.yonsei.ac.kr',
    '고려대학교':     'https://www.korea.ac.kr',
    'KAIST':         'https://www.kaist.ac.kr',
    '한국과학기술원': 'https://www.kaist.ac.kr',
    'POSTECH':       'https://www.postech.ac.kr',
    '포항공과대학교': 'https://www.postech.ac.kr',
    'UNIST':         'https://www.unist.ac.kr',
    'GIST':          'https://www.gist.ac.kr',
    'DGIST':         'https://www.dgist.ac.kr',
    '성균관대학교':   'https://www.skku.edu',
    '한양대학교':     'https://www.hanyang.ac.kr',
    '이화여자대학교': 'https://www.ewha.ac.kr',
    '서강대학교':     'https://www.sogang.ac.kr',
    '중앙대학교':     'https://www.cau.ac.kr',
    '경희대학교':     'https://www.khu.ac.kr',
    '한국외국어대학교':'https://www.hufs.ac.kr',
    '서울시립대학교': 'https://www.uos.ac.kr',
    '건국대학교':     'https://www.konkuk.ac.kr',
    '동국대학교':     'https://www.dongguk.edu',
    '홍익대학교':     'https://www.hongik.ac.kr',
    '국민대학교':     'https://www.kookmin.ac.kr',
    '숙명여자대학교': 'https://www.sookmyung.ac.kr',
    '세종대학교':     'https://www.sejong.ac.kr',
    '단국대학교':     'https://www.dankook.ac.kr',
    '아주대학교':     'https://www.ajou.ac.kr',
    '인하대학교':     'https://www.inha.ac.kr',
    '숭실대학교':     'https://www.ssu.ac.kr',
    '인천대학교':     'https://www.inu.ac.kr',
    '명지대학교':     'https://www.mju.ac.kr',
    '부산대학교':     'https://www.pusan.ac.kr',
    '경북대학교':     'https://www.knu.ac.kr',
    '전남대학교':     'https://www.jnu.ac.kr',
    '전북대학교':     'https://www.jbnu.ac.kr',
    '충남대학교':     'https://www.cnu.ac.kr',
    '충북대학교':     'https://www.chungbuk.ac.kr',
    '가천대학교':     'https://www.gachon.ac.kr',
    '가톨릭대학교':   'https://www.catholic.ac.kr',
    '광운대학교':     'https://www.kw.ac.kr',
    '덕성여자대학교': 'https://www.duksung.ac.kr',
    '동덕여자대학교': 'https://www.dongduk.ac.kr',
    '삼육대학교':     'https://www.syu.ac.kr',
    '상명대학교':     'https://www.smu.ac.kr',
    '서울과학기술대학교': 'https://www.seoultech.ac.kr',
    '서울여자대학교': 'https://www.swu.ac.kr',
    '성공회대학교':   'https://www.skhu.ac.kr',
    '성신여자대학교': 'https://www.sungshin.ac.kr',
    '한국항공대학교': 'https://www.hau.ac.kr',
    '서경대학교':     'https://www.skuniv.ac.kr',
};

// 주요 대학별 학과 홈페이지 URL
const DEPT_URL_MAP = {
    '서울대학교': {
        '컴퓨터공학부':    'https://cse.snu.ac.kr',
        '전기정보공학부':  'https://ee.snu.ac.kr',
        '기계공학부':      'https://me.snu.ac.kr',
        '경영학과':        'https://cba.snu.ac.kr',
        '경영대학':        'https://cba.snu.ac.kr',
        '의과대학':        'https://medicine.snu.ac.kr',
        '법학전문대학원':  'https://law.snu.ac.kr',
        '수학과':          'https://math.snu.ac.kr',
        '물리학과':        'https://physics.snu.ac.kr',
        '화학부':          'https://chem.snu.ac.kr',
        '자유전공학부':    'https://cls.snu.ac.kr',
        '건축학과':        'https://architecture.snu.ac.kr',
        '간호대학':        'https://nursing.snu.ac.kr',
    },
    '연세대학교': {
        '컴퓨터과학과':    'https://cs.yonsei.ac.kr',
        '전기전자공학부':  'https://ee.yonsei.ac.kr',
        '경영대학':        'https://biz.yonsei.ac.kr',
        '의과대학':        'https://medicine.yonsei.ac.kr',
        '법학전문대학원':  'https://law.yonsei.ac.kr',
        '수학과':          'https://math.yonsei.ac.kr',
    },
    '고려대학교': {
        '컴퓨터학과':      'https://cs.korea.ac.kr',
        '전기전자공학부':  'https://ee.korea.ac.kr',
        '경영대학':        'https://biz.korea.ac.kr',
        '의과대학':        'https://medicine.korea.ac.kr',
        '법학전문대학원':  'https://law.korea.ac.kr',
        '수학과':          'https://math.korea.ac.kr',
    },
    'KAIST': {
        '전산학부':        'https://cs.kaist.ac.kr',
        '전기및전자공학부':'https://ee.kaist.ac.kr',
        '수리과학과':      'https://mathsci.kaist.ac.kr',
        '물리학과':        'https://physics.kaist.ac.kr',
    },
    '성균관대학교': {
        '소프트웨어학과':  'https://sw.skku.edu',
        '컴퓨터교육학과':  'https://comedu.skku.edu',
        '전자전기공학부':  'https://ee.skku.edu',
        '경영대학':        'https://biz.skku.edu',
        '의과대학':        'https://medicine.skku.edu',
    },
    '한양대학교': {
        '컴퓨터소프트웨어학부': 'https://cs.hanyang.ac.kr',
        '전기공학과':      'https://ee.hanyang.ac.kr',
        '경영학부':        'https://biz.hanyang.ac.kr',
        '의과대학':        'https://medicine.hanyang.ac.kr',
    },
    '가천대학교': {
        '시스템반도체공학과': 'https://www.gachon.ac.kr/sites/ssd/index.do',
        '컴퓨터공학과':    'https://www.gachon.ac.kr/sites/cse/index.do',
        '의과대학':        'https://www.gachon.ac.kr/sites/med/index.do',
        '간호학과':        'https://www.gachon.ac.kr/sites/nur/index.do',
        '소프트웨어학과':  'https://www.gachon.ac.kr/sites/sw/index.do',
    },
};

// 2026학년도 주요 대학/학과 입결 참고값 (수시 학생부 기준, 70%컷 또는 평균)
const CUTOFF_DATA = {
    '서울대학교': {
        '컴퓨터공학부':    { grade9: 1.2, label: '종합전형 합격 내신 평균' },
        '전기정보공학부':  { grade9: 1.3, label: '종합전형 합격 내신 평균' },
        '경영학과':        { grade9: 1.4, label: '종합전형 합격 내신 평균' },
        '의과대학':        { grade9: 1.1, label: '종합전형 합격 내신 평균' },
        '자유전공학부':    { grade9: 1.3, label: '종합전형 합격 내신 평균' },
        '수학과':          { grade9: 1.5, label: '종합전형 합격 내신 평균' },
    },
    '연세대학교': {
        '컴퓨터과학과':    { grade9: 1.6, label: '추천형 70%컷' },
        '전기전자공학부':  { grade9: 1.8, label: '추천형 70%컷' },
        '경영대학':        { grade9: 1.7, label: '추천형 70%컷' },
        '의과대학':        { grade9: 1.2, label: '추천형 70%컷' },
        '수학과':          { grade9: 2.0, label: '추천형 70%컷' },
    },
    '고려대학교': {
        '컴퓨터학과':      { grade9: 1.7, label: '학교추천 70%컷' },
        '전기전자공학부':  { grade9: 1.9, label: '학교추천 70%컷' },
        '경영대학':        { grade9: 1.8, label: '학교추천 70%컷' },
        '의과대학':        { grade9: 1.2, label: '학교추천 70%컷' },
        '수학과':          { grade9: 2.0, label: '학교추천 70%컷' },
    },
    'KAIST': {
        '전산학부':        { grade9: 1.5, label: '일반전형 내신 참고값' },
        '전기및전자공학부':{ grade9: 1.6, label: '일반전형 내신 참고값' },
        '수리과학과':      { grade9: 1.7, label: '일반전형 내신 참고값' },
    },
    '성균관대학교': {
        '소프트웨어학과':  { grade9: 2.2, label: '학생부교과 70%컷' },
        '전자전기공학부':  { grade9: 2.4, label: '학생부교과 70%컷' },
        '경영대학':        { grade9: 2.0, label: '학생부교과 70%컷' },
        '의과대학':        { grade9: 1.3, label: '학생부교과 70%컷' },
    },
    '한양대학교': {
        '컴퓨터소프트웨어학부': { grade9: 2.3, label: '학생부교과 70%컷' },
        '전기공학과':      { grade9: 2.5, label: '학생부교과 70%컷' },
        '경영학부':        { grade9: 2.1, label: '학생부교과 70%컷' },
        '의과대학':        { grade9: 1.4, label: '학생부교과 70%컷' },
    },
    '이화여자대학교': {
        '컴퓨터공학과':    { grade9: 2.5, label: '고교추천 70%컷' },
        '경영학부':        { grade9: 2.3, label: '고교추천 70%컷' },
        '의과대학':        { grade9: 1.5, label: '고교추천 70%컷' },
    },
    '서강대학교': {
        '컴퓨터공학과':    { grade9: 2.4, label: '학생부교과 70%컷' },
        '경영학부':        { grade9: 2.2, label: '학생부교과 70%컷' },
    },
    '중앙대학교': {
        '소프트웨어학부':  { grade9: 2.8, label: '학생부교과 70%컷' },
        '경영학부':        { grade9: 2.6, label: '학생부교과 70%컷' },
        '의과대학':        { grade9: 1.5, label: '학생부교과 70%컷' },
    },
    '경희대학교': {
        '컴퓨터공학부':    { grade9: 3.0, label: '고교연계 70%컷' },
        '경영학과':        { grade9: 3.2, label: '고교연계 70%컷' },
        '의과대학':        { grade9: 1.6, label: '고교연계 70%컷' },
    },
    '한국외국어대학교': {
        '영어대학':        { grade9: 2.5, label: '학생부교과 70%컷' },
        '경영대학':        { grade9: 2.8, label: '학생부교과 70%컷' },
    },
    '서울시립대학교': {
        '컴퓨터과학부':    { grade9: 2.6, label: '학생부교과 70%컷' },
        '경영학부':        { grade9: 2.8, label: '학생부교과 70%컷' },
    },
    '건국대학교': {
        '컴퓨터공학부':    { grade9: 3.5, label: '학생부교과 70%컷' },
        '경영학부':        { grade9: 3.3, label: '학생부교과 70%컷' },
    },
    '동국대학교': {
        '컴퓨터공학과':    { grade9: 3.4, label: '학생부교과 70%컷' },
        '경영학과':        { grade9: 3.6, label: '학생부교과 70%컷' },
    },
    '인하대학교': {
        '컴퓨터공학과':    { grade9: 3.2, label: '학생부교과 70%컷' },
        '전기공학과':      { grade9: 3.4, label: '학생부교과 70%컷' },
        '의과대학':        { grade9: 1.8, label: '학생부교과 70%컷' },
    },
    '아주대학교': {
        '소프트웨어학과':  { grade9: 3.5, label: '학생부교과 70%컷' },
        '전자공학과':      { grade9: 3.7, label: '학생부교과 70%컷' },
        '의과대학':        { grade9: 1.7, label: '학생부교과 70%컷' },
    },
    '숭실대학교': {
        '컴퓨터학부':      { grade9: 3.8, label: '학생부교과 70%컷' },
        '소프트웨어학부':  { grade9: 3.6, label: '학생부교과 70%컷' },
    },
    '국민대학교': {
        '소프트웨어학부':  { grade9: 3.9, label: '학생부교과 70%컷' },
        '컴퓨터공학부':    { grade9: 4.0, label: '학생부교과 70%컷' },
    },
    '세종대학교': {
        '컴퓨터공학과':    { grade9: 3.8, label: '학생부교과 70%컷' },
        '소프트웨어학과':  { grade9: 3.6, label: '학생부교과 70%컷' },
    },
    '단국대학교': {
        '소프트웨어학과':  { grade9: 4.0, label: '학생부교과 70%컷' },
        '컴퓨터공학과':    { grade9: 4.1, label: '학생부교과 70%컷' },
    },
    '서울과학기술대학교': {
        '컴퓨터공학과':    { grade9: 3.5, label: '학생부교과 70%컷' },
        '전기정보공학과':  { grade9: 3.6, label: '학생부교과 70%컷' },
    },
    '광운대학교': {
        '컴퓨터공학부':    { grade9: 3.9, label: '학생부교과 70%컷' },
        '소프트웨어학부':  { grade9: 3.7, label: '학생부교과 70%컷' },
    },
    '가천대학교': {
        '시스템반도체공학과': { grade9: 3.0, label: '교과전형 합격 내신 분포 (2~3등급대)' },
        '컴퓨터공학과':    { grade9: 4.0, label: '학생부교과 70%컷' },
        '의과대학':        { grade9: 1.8, label: '학생부교과 70%컷' },
        '소프트웨어학과':  { grade9: 4.1, label: '학생부교과 70%컷' },
    },
    '부산대학교': {
        '컴퓨터공학과':    { grade9: 3.1, label: '학생부교과 70%컷' },
        '전자전기공학부':  { grade9: 3.2, label: '학생부교과 70%컷' },
        '의과대학':        { grade9: 1.7, label: '학생부교과 70%컷' },
    },
    '경북대학교': {
        '컴퓨터학부':      { grade9: 3.3, label: '학생부교과 70%컷' },
        '전자공학부':      { grade9: 3.4, label: '학생부교과 70%컷' },
        '의과대학':        { grade9: 1.8, label: '학생부교과 70%컷' },
    },
};

// 경기진협 2028 시행계획 나침반 — 대학별 PDF 직접 링크 (구글 드라이브)
const UNI_PLAN_URL = {
    '가천대학교':        'https://drive.google.com/open?id=1e6JayrALWW2Smzli4M8zd7Pq7dpx2g5C',
    '가톨릭대학교':      'https://drive.google.com/open?id=1-vdDECCcglZ2ZRT2gTzwbjC1ILCdjgGp',
    '건국대학교':        'https://drive.google.com/open?id=1oiV1aENYl0xBznkpPrDST5EpXzlEGisK',
    '경희대학교':        'https://drive.google.com/open?id=1gGE2Ua8wI9kDTrPPsJ22ZnQIApHR760t',
    '고려대학교':        'https://drive.google.com/open?id=1d007JpZi2EMpe2AKIGOfWXwMMQfbZ6Jl',
    '광운대학교':        'https://drive.google.com/open?id=1KSTWnOKI1swNg5q_L41jnDUqkMVk41cm',
    '국민대학교':        'https://drive.google.com/open?id=1YB6ePfrXmqB5HMDcoGAtUFhoe-c1lJls',
    '단국대학교':        'https://drive.google.com/open?id=1Fe7ccQX5v8aCxC1j46-QkMmaYdFoLctS',
    '덕성여자대학교':    'https://drive.google.com/open?id=1FVjCqNzkF5taSwPlNNU8hwXAtCtb2L1m',
    '동국대학교':        'https://drive.google.com/open?id=1-8dyqXRbDkWOioKV83jZXtcldQgBSulE',
    '동덕여자대학교':    'https://drive.google.com/open?id=1ghbUYgrtGQx_oCVgpQd6gXGkvUK3pxNB',
    '명지대학교':        'https://drive.google.com/open?id=1pN7aR--I_8xKIkzV8VL9czbQYfH-ED22',
    '부산대학교':        'https://drive.google.com/file/d/1npqTopTsZW1mW4M2lDzBOp3PH9wwJcZU/view?usp=drive_link',
    '삼육대학교':        'https://drive.google.com/open?id=1yRUZbsIyycMZy2AU5fPJMn1XsnuxQzEy',
    '상명대학교':        'https://drive.google.com/open?id=1jFnVSgAM1NUkFg8JsYB_WfmPI1bsSQYX',
    '서강대학교':        'https://drive.google.com/open?id=1iLtNCPMqk751nXsyD8wgEha0qWPSwuSQ',
    '서울과학기술대학교':'https://drive.google.com/open?id=19cQ7yW6eSJeiQGg1THLc7er5UClQmyMR',
    '서울대학교':        'https://drive.google.com/open?id=1bvEkkRsWvn5PDJvtICZ7xqAV-8dG3cfQ',
    '서울시립대학교':    'https://drive.google.com/open?id=1GTFDkV1BxnQZyVw-7SGau1H2cz6dZWw8',
    '서울여자대학교':    'https://drive.google.com/open?id=1KT9vFZZOkmJqVTFlkd5xs0yNAZBA5heE',
    '성균관대학교':      'https://drive.google.com/open?id=1rB-RUieTYBroJ9CQiP3eB2FSS8QOF7hU',
    '성공회대학교':      'https://drive.google.com/open?id=1f-JaNGwqhoj5wRpVPaHz8kR8c8oSXt',
    '성신여자대학교':    'https://drive.google.com/open?id=1gU0XVoGiHNL4vnCEKI69bSZN_O1b4gHT',
    '세종대학교':        'https://drive.google.com/open?id=1YfV_KCxA1ANe3waidwHMvy5NoDWPuWrD',
    '숙명여자대학교':    'https://drive.google.com/open?id=1gK0X4gIRZQc_njXTIw6qPBsz5RUNQU-o',
    '숭실대학교':        'https://drive.google.com/open?id=1X56oSxZ-4RsYAwSnaZueS_duBtx1Yj49',
    '아주대학교':        'https://drive.google.com/open?id=10_r1wV8fnH7Cl0ZluaFtfVO4PsD-Tuvj',
    '연세대학교':        'https://drive.google.com/open?id=1yPVslVag5sEUrrXURemqNATiwFAgTpCX',
    '이화여자대학교':    'https://drive.google.com/open?id=1UA-BochF7_x3D5ZUDRnrNhtKMD6ZZqPD',
    '인천대학교':        'https://drive.google.com/open?id=1IbGH77ZtJvdmwrnqezwSY8iJqTJFOtRK',
    '인하대학교':        'https://drive.google.com/open?id=1krndaYhMEqrtEDO2-NwgwZT6R-CkgXMH',
    '전남대학교':        'https://drive.google.com/file/d/1cIpvRgL0src-iSlpyqqUnlQl_2Iiqzym/view?usp=drive_link',
    '전북대학교':        'https://drive.google.com/open?id=155SYHT5jF3kAMToms1UECmQcLEFX6qlr',
    '중앙대학교':        'https://drive.google.com/open?id=17IHwSINrAaUb8F9WzTkyi2b1r0SK5FzZ',
    '충남대학교':        'https://drive.google.com/open?id=1HLYQmFQNUzslk_wwA8EciFyDAus6y8cA',
    '충북대학교':        'https://drive.google.com/open?id=1j9AIjyMFe_bdmaPlf-3TVSi-meC4ua2F',
    'POSTECH':           'https://drive.google.com/open?id=1kYe5WH2V7uleOFHSx7ME14WqfdhppOO0',
    '포항공과대학교':    'https://drive.google.com/open?id=1kYe5WH2V7uleOFHSx7ME14WqfdhppOO0',
    '한국외국어대학교':  'https://drive.google.com/open?id=18D47sENDi2Yq7W_SeRI8mOzlRSro58uG',
    '한국항공대학교':    'https://drive.google.com/open?id=1YUU4wJ9L8I7LzyH0cudbQFkoHgAFJJ2-',
    '한양대학교':        'https://drive.google.com/open?id=1L9GDoXkwtyU3pSDWpI-uarpPnDzbPQSZ',
    '홍익대학교':        'https://drive.google.com/open?id=1iWJU_uR5reI4JWpSombXZHwUlYfm7m7w',
};

// 대학별 입학처 홈페이지 URL (2028 시행계획 게시 위치)
const UNI_ADMISSION_URL = {
    '서울대학교':        'https://admission.snu.ac.kr',
    '연세대학교':        'https://admission.yonsei.ac.kr/seoul/admission/html/main/main.asp',
    '고려대학교':        'https://oku.korea.ac.kr/oku/index.do',
    'KAIST':             'https://admission.kaist.ac.kr',
    '한국과학기술원':    'https://admission.kaist.ac.kr',
    'POSTECH':           'https://admission.postech.ac.kr',
    '포항공과대학교':    'https://admission.postech.ac.kr',
    'UNIST':             'https://admissions.unist.ac.kr',
    'GIST':              'https://admission.gist.ac.kr',
    'DGIST':             'https://admission.dgist.ac.kr',
    '성균관대학교':      'https://admission.skku.edu',
    '한양대학교':        'https://admission.hanyang.ac.kr',
    '이화여자대학교':    'https://admission.ewha.ac.kr',
    '서강대학교':        'https://admission.sogang.ac.kr',
    '중앙대학교':        'https://admission.cau.ac.kr',
    '경희대학교':        'https://ipsi.khu.ac.kr',
    '한국외국어대학교':  'https://adms.hufs.ac.kr',
    '서울시립대학교':    'https://admission.uos.ac.kr',
    '건국대학교':        'https://enter.konkuk.ac.kr',
    '동국대학교':        'https://ipsi.dongguk.edu',
    '홍익대학교':        'https://ipsi.hongik.ac.kr',
    '국민대학교':        'https://admission.kookmin.ac.kr',
    '숙명여자대학교':    'https://admission.sookmyung.ac.kr',
    '세종대학교':        'https://ipsi.sejong.ac.kr',
    '단국대학교':        'https://admission.dankook.ac.kr',
    '아주대학교':        'https://admission.ajou.ac.kr',
    '인하대학교':        'https://admission.inha.ac.kr',
    '숭실대학교':        'https://admission.ssu.ac.kr',
    '인천대학교':        'https://admission.inu.ac.kr',
    '명지대학교':        'https://admission.mju.ac.kr',
    '부산대학교':        'https://ipsi.pusan.ac.kr',
    '경북대학교':        'https://admission.knu.ac.kr',
    '전남대학교':        'https://admission.jnu.ac.kr',
    '전북대학교':        'https://admission.jbnu.ac.kr',
    '충남대학교':        'https://admission.cnu.ac.kr',
    '충북대학교':        'https://admission.chungbuk.ac.kr',
    '가천대학교':        'https://admission.gachon.ac.kr',
    '가톨릭대학교':      'https://admission.catholic.ac.kr',
    '광운대학교':        'https://admission.kw.ac.kr',
    '서울과학기술대학교':'https://admission.seoultech.ac.kr',
    '서울여자대학교':    'https://admission.swu.ac.kr',
    '성신여자대학교':    'https://ipsi.sungshin.ac.kr',
    '덕성여자대학교':    'https://admission.duksung.ac.kr',
    '동덕여자대학교':    'https://ipsi.dongduk.ac.kr',
    '한국항공대학교':    'https://admission.hau.ac.kr',
    '상명대학교':        'https://ipsi.smu.ac.kr',
};

// 2028학년도 주요 대학 수능최저학력기준 (시행계획 발표 기준)
// null = 시행계획 PDF 직접 확인 필요
const UNI_CSAT_MIN = {
    '서울대학교': {
        교과: '없음 (지역균형전형 수능최저 폐지)',
        종합: '없음'
    },
    '연세대학교': {
        교과: '추천형: 없음',
        종합: '종합인재형: 국·수 포함 3개 합 6이내, 영어 3등급, 한국사 4등급'
    },
    '고려대학교': {
        교과: '학교추천: 없음',
        종합: '학업우수형: 4개 영역 중 3개 합 7이내 (2026 기준 참고)'
    },
    '성균관대학교': {
        교과: '3개 영역 합 7이내 (의약학 별도 기준 적용)',
        종합: '없음'
    },
    '한양대학교': {
        교과: '없음',
        종합: '없음'
    },
    '이화여자대학교': {
        교과: '고교추천: 3개 합 7이내 (2026 기준 참고)',
        종합: '없음'
    },
    '서강대학교': {
        교과: '지역균형: 3개 합 6이내, 영어 2등급 (2026 기준 참고)',
        종합: '없음'
    },
    '중앙대학교': {
        교과: '일반: 3개 합 6~7 / 의약학: 4개 합 5',
        종합: '성장형인재: 3개 합 6 / 의약학: 4개 합 5'
    },
    '경희대학교': {
        교과: '지역균형: 2개 합 5이내 (탐구: 통합사회·통합과학 中 1과목)',
        종합: '의약학 네오르네상스: 국·수·탐 中 3개 합 4이내'
    },
    '한국외국어대학교': {
        교과: '학교장추천: 2개 합 6이내 (2026 기준 참고)',
        종합: '없음'
    },
    '서울시립대학교': {
        교과: '지역균형: 2개 합 5이내 (2026 기준 참고)',
        종합: '없음'
    },
    '건국대학교': {
        교과: 'KU지역균형: 2개 합 5이내 (2026 기준 참고)',
        종합: '없음'
    },
    '동국대학교': {
        교과: '학교장추천인재: 3개 합 6이내 (2026 기준 참고)',
        종합: '없음'
    },
    '인하대학교': {
        교과: '지역균형: 2개 합 6이내 (2026 기준 참고)',
        종합: '없음'
    },
    '아주대학교': {
        교과: '고교추천: 3개 합 7이내 (2026 기준 참고)',
        종합: '없음'
    },
    '가천대학교': {
        교과: '교과우수자: 3개 합 6이내 / 의약학: 4개 합 5이내 (2026 기준 참고)',
        종합: '없음 (의예과 제외)'
    },
    '부산대학교': {
        교과: '학생부교과: 2개 합 5이내 (2026 기준 참고)',
        종합: '없음'
    },
    '경북대학교': {
        교과: '교과우수자: 2개 합 7이내 (2026 기준 참고)',
        종합: '없음'
    },
};

// 2028 학과계열별 주요 과목 (교과전형·종합전형)
const SUBJECT_DATA = [
    {
        keywords: ['컴퓨터', '소프트웨어', '인공지능', 'AI', '정보보안', '사이버', '데이터', 'SW', '정보통신'],
        label: '컴퓨터·소프트웨어·AI 계열',
        교과: {
            과목: ['수학(미적분·기하)', '영어', '물리학', '정보'],
            메모: '수능최저: 수학+영어 각 2등급 내외 (대학별 상이)'
        },
        종합: {
            권장과목: ['수학Ⅱ·미적분', '물리학Ⅱ', '정보'],
            역량: '수학·논리적 사고력, SW·프로그래밍 관심, 문제해결 탐구 활동'
        }
    },
    {
        keywords: ['반도체', '시스템반도체', '전기', '전자', '전파', '제어', '회로', '광전자'],
        label: '전기·전자·반도체 계열',
        교과: {
            과목: ['수학(미적분·기하)', '물리학', '영어', '화학'],
            메모: '수능최저: 수학+영어 각 2등급 내외 / 수학 비중 높음'
        },
        종합: {
            권장과목: ['수학Ⅱ·미적분·기하', '물리학Ⅱ', '화학Ⅱ'],
            역량: '물리·수학 탐구 역량, 전자·회로 관심, 실험·설계 활동'
        }
    },
    {
        keywords: ['기계', '자동차', '항공', '로봇', '메카트로닉스', '나노', '산업공학', '제조'],
        label: '기계·자동차·항공 계열',
        교과: {
            과목: ['수학(미적분·기하)', '물리학', '영어', '화학'],
            메모: '수능최저: 수학+영어 2~3등급 내외'
        },
        종합: {
            권장과목: ['수학Ⅱ·미적분·기하', '물리학Ⅱ', '화학Ⅰ'],
            역량: '역학·공학적 사고력, 설계·제작 탐구 활동'
        }
    },
    {
        keywords: ['의학', '의과', '의예', '간호', '약학', '치의', '한의', '수의', '보건', '임상'],
        label: '의학·간호·약학 계열',
        교과: {
            과목: ['수학(미적분)', '화학', '생명과학', '영어'],
            메모: '수능최저 기준 엄격 — 수학+과학 각 1~2등급 요구 많음'
        },
        종합: {
            권장과목: ['수학Ⅱ·미적분', '화학Ⅱ', '생명과학Ⅱ'],
            역량: '생명·의학 탐구, 봉사·의료 관련 활동, 과학 심화 역량'
        }
    },
    {
        keywords: ['경영', '경제', '회계', '금융', '무역', '비즈니스', '마케팅', '유통'],
        label: '경영·경제·금융 계열',
        교과: {
            과목: ['수학(확률·통계)', '영어', '사회(경제)', '국어'],
            메모: '수능최저: 영어 1~2등급 요구 다수'
        },
        종합: {
            권장과목: ['수학Ⅱ', '경제', '영어'],
            역량: '논리적 사고·리더십, 경제·사회 이슈 탐구, 시사 관심'
        }
    },
    {
        keywords: ['법학', '법률', '법과'],
        label: '법학 계열',
        교과: {
            과목: ['국어', '영어', '사회(법과 정치)', '수학'],
            메모: '수능최저: 국어·영어 중시'
        },
        종합: {
            권장과목: ['국어', '사회·법과 정치', '영어'],
            역량: '논리적 글쓰기·토론, 사회·법 이슈 탐구, 독서 활동'
        }
    },
    {
        keywords: ['수학', '통계', '수리', '응용수학'],
        label: '수학·통계 계열',
        교과: {
            과목: ['수학(미적분·기하·확률통계)', '물리학', '영어'],
            메모: '수학 전 영역 내신 우수성 핵심'
        },
        종합: {
            권장과목: ['수학Ⅱ·미적분·기하', '물리학Ⅰ'],
            역량: '수학 심화 탐구, 수학올림피아드·경시대회, 증명·논리 활동'
        }
    },
    {
        keywords: ['물리', '천문', '지구과학'],
        label: '물리학·천문·지구과학 계열',
        교과: {
            과목: ['수학(미적분·기하)', '물리학', '화학', '영어'],
            메모: '물리학 내신 필수, 수학 심화 병행'
        },
        종합: {
            권장과목: ['수학Ⅱ·미적분·기하', '물리학Ⅱ', '화학Ⅰ'],
            역량: '물리 실험·탐구, 과학 심화 활동, 수리적 사고력'
        }
    },
    {
        keywords: ['화학', '화공', '신소재', '재료', '고분자', '섬유'],
        label: '화학·화공·신소재 계열',
        교과: {
            과목: ['수학(미적분)', '화학', '물리학', '영어'],
            메모: '화학 내신 필수, 수학·물리 병행'
        },
        종합: {
            권장과목: ['수학Ⅱ·미적분', '화학Ⅱ', '물리학Ⅰ'],
            역량: '화학 실험·탐구, 소재·재료 관련 관심, 과학 심화 역량'
        }
    },
    {
        keywords: ['생물', '생명', '바이오', '식품', '환경', '생태', '농학', '원예'],
        label: '생명과학·바이오·환경 계열',
        교과: {
            과목: ['생명과학', '화학', '수학', '영어'],
            메모: '생명과학·화학 내신 중시'
        },
        종합: {
            권장과목: ['생명과학Ⅱ', '화학Ⅱ', '수학Ⅱ'],
            역량: '생명·환경 탐구·실험, 관련 대회·봉사 활동'
        }
    },
    {
        keywords: ['건축', '도시', '토목', '도시공학', '조경'],
        label: '건축·도시·토목 계열',
        교과: {
            과목: ['수학(미적분)', '물리학', '영어', '미술(건축)'],
            메모: '건축학과는 포트폴리오·미술 역량도 반영'
        },
        종합: {
            권장과목: ['수학Ⅱ·미적분', '물리학Ⅰ', '미술'],
            역량: '공간·구조 탐구, 설계·드로잉 활동, 환경·사회 관심'
        }
    },
    {
        keywords: ['국어', '한국어', '국문', '문예', '한문', '문학', '언어'],
        label: '국어·국문·문예창작 계열',
        교과: {
            과목: ['국어', '영어', '사회', '수학'],
            메모: '국어 내신 최우선, 독서·글쓰기 이력 중시'
        },
        종합: {
            권장과목: ['국어 심화', '사회', '영어'],
            역량: '독서·문학 탐구, 글쓰기·창작 활동, 언어 감수성'
        }
    },
    {
        keywords: ['영어', '영문', '영미', '외국어', '불어', '독어', '중어', '일어', '스페인', '노어', '아랍'],
        label: '외국어·영어 계열',
        교과: {
            과목: ['영어', '국어', '제2외국어', '사회'],
            메모: '영어 내신 최우선, 제2외국어 선택 유리'
        },
        종합: {
            권장과목: ['영어', '국어', '제2외국어'],
            역량: '언어·문화 탐구, 교류·국제 관련 활동, 외국어 역량'
        }
    },
    {
        keywords: ['사회', '행정', '정치', '사회학', '사회복지', '심리', '상담'],
        label: '사회·행정·심리 계열',
        교과: {
            과목: ['사회(생활과 윤리·사회문화)', '국어', '영어', '수학'],
            메모: '사회 과목 내신·탐구 이력 중시'
        },
        종합: {
            권장과목: ['사회·생활과 윤리', '국어', '영어'],
            역량: '사회 현상 탐구, 봉사·공동체 활동, 비판적 사고'
        }
    },
    {
        keywords: ['교육', '사범', '교대', '유아', '초등'],
        label: '교육·사범 계열',
        교과: {
            과목: ['국어', '수학', '영어', '전공 관련 교과'],
            메모: '전공별 주요 교과 내신 필수 (예: 수학교육 → 수학)'
        },
        종합: {
            권장과목: ['국어', '수학·영어 (전공별)', '사회'],
            역량: '교육 봉사·튜터링, 전공 교과 심화, 소통·리더십 활동'
        }
    },
    {
        keywords: ['미술', '디자인', '시각', '산업디자인', '패션', '영상', '애니'],
        label: '미술·디자인·영상 계열',
        교과: {
            과목: ['미술', '국어', '영어', '사회'],
            메모: '실기·포트폴리오 반영 전형 병행 다수'
        },
        종합: {
            권장과목: ['미술', '국어', '영어'],
            역량: '작품 활동·포트폴리오, 시각적 창의성, 예술·문화 탐구'
        }
    },
    {
        keywords: ['음악', '성악', '피아노', '작곡', '체육', '스포츠', '운동'],
        label: '음악·체육·예술 계열',
        교과: {
            과목: ['예체능 관련 교과', '국어', '영어'],
            메모: '실기 비중 매우 높음, 교과는 최저 조건 수준'
        },
        종합: {
            권장과목: ['예체능 관련 교과'],
            역량: '실기 수련·수상 이력, 예술·체육 관련 활동 전반'
        }
    },
];

// 대학명 → adiga.kr unvCd 매핑
const UNIV_CODE_MAP = {
    // 서울
    '가톨릭대학교': '0000007', '건국대학교': '0000011', '경희대학교': '0000065',
    '고려대학교': '0000069', '광운대학교': '0000073', '국민대학교': '0000078',
    '동국대학교': '0000100', '명지대학교': '0000111',
    '서강대학교': '0000120', '서울과학기술대학교': '0000125', '서울대학교': '0000019',
    '서울시립대학교': '0000040', '서경대학교': '0000121',
    '성균관대학교': '0000133', '성신여자대학교': '0000143',
    '세종대학교': '0000145', '숙명여자대학교': '0000147', '숭실대학교': '0000148',
    '연세대학교': '0000149', '이화여자대학교': '0000163', '중앙대학교': '0000175',
    '한국외국어대학교': '0000192', '한성대학교': '0000200', '한양대학교': '0000203',
    '홍익대학교': '0000212',
    '덕성여자대학교': '0000099', '동덕여자대학교': '0000103',
    '삼육대학교': '0000116', '상명대학교': '0000119',
    '서울여자대학교': '0000128', '성공회대학교': '0000136',
    // 경기/인천
    '가천대학교': '0000063', '경기대학교': '0000056',
    '단국대학교(죽전)': '0000087', '아주대학교': '0000156',
    '인하대학교': '0000169', '인천대학교': '0000170',
    '한국항공대학교': '0000194',
    // 수도권 분교
    '연세대학교(미래)': '0000150', '고려대학교(세종)': '0000070',
    // 강원
    '강원대학교': '0000009', '한림대학교': '0000196', '가톨릭관동대학교': '0000008',
    // 충청
    '충남대학교': '0000029', '충북대학교': '0000181',
    '공주대학교': '0000072', '순천향대학교': '0000146',
    '단국대학교(천안)': '0000088', '한국교원대학교': '0000187',
    '한국기술교육대학교': '0000189', '건양대학교': '0000012',
    '호서대학교': '0000207', '한밭대학교': '0000198',
    // 호남
    '전남대학교': '0000173', '전북대학교': '0000174',
    '전주교육대학교': '0000258', '진주교육대학교': '0000260',
    '조선대학교': '0000172', '목포대학교': '0000113',
    '군산대학교': '0000079', '순천대학교': '0000144', '우석대학교': '0000161',
    // 대구/경북
    '경북대학교': '0000057', '영남대학교': '0000151',
    '계명대학교': '0000060', '대구가톨릭대학교': '0000082',
    '대구대학교': '0000084', '안동대학교': '0000153',
    '동국대학교(경주)': '0000101',
    // 경남/부산/울산
    '부산대학교': '0000025', '경상국립대학교': '0000064',
    '동아대학교': '0000104', '부경대학교': '0000024',
    '경성대학교': '0000062', '동의대학교': '0000106',
    '울산대학교': '0000158', '인제대학교': '0000168',
    '신라대학교': '0000141', '경남대학교': '0000054',
    // 제주
    '제주대학교': '0000178',
};

// 메인 애플리케이션 로직
class BucketListApp {
    constructor() {
        this.currentFilter = 'all';
        this.editingId = null;
        this.selectedId = null;
        this.init();
    }

    /**
     * 앱 초기화
     */
    init() {
        this.cacheElements();
        this.uniNames = Object.keys(UNIV_CODE_MAP).sort((a, b) => a.localeCompare(b, 'ko'));
        this.bindEvents();
        this.render();
    }

    /**
     * 대학명 입력값에 맞는 자동완성 목록 표시
     */
    renderUniSuggestions() {
        const q = this.uniInput.value.trim();
        const matches = q
            ? this.uniNames.filter(name => name.includes(q)).slice(0, 8)
            : this.uniNames.slice(0, 8);

        if (matches.length === 0) {
            this.hideUniSuggestions();
            return;
        }

        this.uniSuggestions.innerHTML = matches
            .map(name => `<li data-name="${this.escapeHtml(name)}" class="px-3 py-2 cursor-pointer hover:bg-violet-50 active:bg-violet-100">${this.escapeHtml(name)}</li>`)
            .join('');
        this.uniSuggestions.classList.remove('hidden');
    }

    hideUniSuggestions() {
        this.uniSuggestions.classList.add('hidden');
    }

    /**
     * DOM 요소 캐싱
     */
    cacheElements() {
        // 폼 요소
        this.bucketForm = document.getElementById('bucketForm');
        this.uniInput = document.getElementById('uniInput');
        this.uniSuggestions = document.getElementById('uniSuggestions');
        this.deptInput = document.getElementById('deptInput');

        // 정보 버튼 / 지도
        this.locationBtn  = document.getElementById('locationBtn');
        this.homepageBtn  = document.getElementById('homepageBtn');
        this.admissionBtn = document.getElementById('admissionBtn');
        this.gradeBtn     = document.getElementById('gradeBtn');
        this.selectedLabel = document.getElementById('selectedLabel');
        this.closeMapBtn       = document.getElementById('closeMap');
        this.mapSection        = document.getElementById('mapSection');
        this.mapFrame          = document.getElementById('mapFrame');
        this.mapTitle          = document.getElementById('mapTitle');
        this.admissionSection  = document.getElementById('admissionSection');
        this.closeAdmissionBtn = document.getElementById('closeAdmission');
        this.subjectTableSection = document.getElementById('subjectTableSection');
        this.uniPlanLinkWrap   = document.getElementById('uniPlanLinkWrap');
        this.uniPlanLink       = document.getElementById('uniPlanLink');
        this.uniAdmLinkWrap    = document.getElementById('uniAdmLinkWrap');
        this.uniAdmLink        = document.getElementById('uniAdmLink');

        // 리스트 컨테이너
        this.bucketListContainer = document.getElementById('bucketListContainer');
        this.listHint = document.getElementById('listHint');
        this.emptyState = document.getElementById('emptyState');


        // 수정 모달 요소
        this.editModal = document.getElementById('editModal');
        this.editForm = document.getElementById('editForm');
        this.editInput = document.getElementById('editInput');
        this.cancelEditBtn = document.getElementById('cancelEdit');

        // 등급 모달 요소
        this.gradeModal = document.getElementById('gradeModal');
        this.gradeModalLabel = document.getElementById('gradeModalLabel');
        this.gradeInput = document.getElementById('gradeInput');
        this.gradeInputHint = document.getElementById('gradeInputHint');
        this.cancelGradeBtn = document.getElementById('cancelGrade');
        this.gradeModalMusicBtn = document.getElementById('gradeModalMusicBtn');
        this.submitGradeBtn = document.getElementById('submitGrade');
        this.gradeResultModal = document.getElementById('gradeResultModal');
        this.gradeResultCard = document.getElementById('gradeResultCard');
        this.gradeResultIcon = document.getElementById('gradeResultIcon');
        this.gradeResultTitle = document.getElementById('gradeResultTitle');
        this.gradeResultContent = document.getElementById('gradeResultContent');
        this.closeGradeResultBtn = document.getElementById('closeGradeResult');

        // API 키 모달 요소
        this.openApiKeyBtn  = document.getElementById('openApiKeyBtn');
        this.apiKeyModal    = document.getElementById('apiKeyModal');
        this.apiKeyInput    = document.getElementById('apiKeyInput');
        this.cancelApiKeyBtn = document.getElementById('cancelApiKey');
        this.saveApiKeyBtn  = document.getElementById('saveApiKey');
    }

    /**
     * 이벤트 바인딩
     */
    bindEvents() {
        // 폼 제출 이벤트
        this.bucketForm.addEventListener('submit', (e) => this.handleAdd(e));

        // 대학명 자동완성 이벤트
        this.uniInput.addEventListener('input', () => this.renderUniSuggestions());
        this.uniInput.addEventListener('focus', () => this.renderUniSuggestions());
        this.uniInput.addEventListener('blur', () => setTimeout(() => this.hideUniSuggestions(), 150));
        this.uniSuggestions.addEventListener('mousedown', (e) => {
            const li = e.target.closest('li[data-name]');
            if (!li) return;
            e.preventDefault();
            this.uniInput.value = li.dataset.name;
            this.hideUniSuggestions();
            this.deptInput.focus();
        });

        // 정보 버튼 이벤트
        this.locationBtn.addEventListener('click',  () => this.handleLocationSearch());
        this.homepageBtn.addEventListener('click',  () => this.handleHomepage());
        this.admissionBtn.addEventListener('click', () => this.handleAdmission());
        this.gradeBtn.addEventListener('click',     () => this.handleGrade());
        this.closeMapBtn.addEventListener('click',       () => this.mapSection.classList.add('hidden'));
        this.closeAdmissionBtn.addEventListener('click', () => this.admissionSection.classList.add('hidden'));
        this.uniPlanLink.addEventListener('click', () => {
            if (this._planPopupUrl) {
                window.open(this._planPopupUrl, 'planPdfPopup', 'width=1000,height=800,scrollbars=yes,resizable=yes');
            }
        });

        // 수정 모달 이벤트
        this.editForm.addEventListener('submit', (e) => this.handleEditSubmit(e));
        this.cancelEditBtn.addEventListener('click', () => this.closeEditModal());
        this.editModal.addEventListener('click', (e) => {
            if (e.target === this.editModal) this.closeEditModal();
        });

        // 등급 모달 이벤트
        this.cancelGradeBtn.addEventListener('click', () => this.closeGradeModal());
        this.gradeModalMusicBtn.addEventListener('click', () => {
            const info = this.getSelectedUni();
            const params = new URLSearchParams();
            if (info) {
                const code = UNIV_CODE_MAP[info.uni];
                if (code) params.set('unvCd', code);
                if (info.uni)  params.set('univName', info.uni);
                if (info.dept) params.set('dept', info.dept);
            }
            const gradeVal = this.gradeInput.value.trim();
            if (gradeVal) params.set('myGrade', gradeVal);
            const gradeSystem = document.querySelector('input[name="gradeSystem"]:checked')?.value || '5';
            params.set('gradeSystem', gradeSystem);
            const url = '합격등급비교.html' + (params.toString() ? '?' + params : '');
            const popup = window.open(url, 'gradeCompare', 'width=1280,height=860,scrollbars=yes,resizable=yes');
            if (!popup) alert('팝업이 차단되었습니다. 브라우저 주소창 오른쪽의 팝업 허용 버튼을 클릭해 주세요.');
        });
        this.submitGradeBtn?.addEventListener('click', () => this.submitGradeCheck());
        this.gradeInput.addEventListener('keydown', (e) => { if (e.key === 'Enter') this.submitGradeCheck(); });

        // API 키 모달 이벤트
        this.openApiKeyBtn?.addEventListener('click', () => this.openApiKeyModal());
        this.cancelApiKeyBtn?.addEventListener('click', () => this.closeApiKeyModal());
        this.saveApiKeyBtn?.addEventListener('click', () => this.saveApiKey());
        this.apiKeyModal?.addEventListener('click', (e) => { if (e.target === this.apiKeyModal) this.closeApiKeyModal(); });
        this.gradeModal.addEventListener('click', (e) => {
            if (e.target === this.gradeModal) this.closeGradeModal();
        });
        this.closeGradeResultBtn.addEventListener('click', () => {
            this.gradeResultModal.classList.add('hidden');
            this.gradeResultModal.classList.remove('flex');
        });
        this.gradeResultModal.addEventListener('click', (e) => {
            if (e.target === this.gradeResultModal) {
                this.gradeResultModal.classList.add('hidden');
                this.gradeResultModal.classList.remove('flex');
            }
        });
        document.querySelectorAll('input[name="gradeSystem"]').forEach(radio => {
            radio.addEventListener('change', (e) => {
                const is9 = e.target.value === '9';
                this.gradeInput.max = is9 ? '9' : '5';
                this.gradeInput.placeholder = is9 ? '예) 2.5' : '예) 2.5';
                this.gradeInputHint.textContent = is9 ? '1~9 등급 입력 (소수점 가능)' : '1~5 등급 입력 (소수점 가능)';
            });
        });
    }

    /**
     * 새 버킷 리스트 추가 처리
     */
    handleAdd(e) {
        e.preventDefault();

        const uni = this.uniInput.value.trim();
        const dept = this.deptInput.value.trim();

        if (!uni || !dept) {
            alert('대학명과 학과를 모두 입력해주세요!');
            return;
        }

        BucketStorage.addItem(`${uni}||${dept}`);
        this.uniInput.value = '';
        this.deptInput.value = '';
        this.hideUniSuggestions();
        this.uniInput.focus();
        this.render();
    }

    /**
     * 완료 상태 토글
     */
    handleToggle(id) {
        BucketStorage.toggleComplete(id);
        this.render();
    }

    /**
     * 수정 모달 열기
     */
    openEditModal(id, currentTitle) {
        this.editingId = id;
        const div = document.createElement('div');
        div.innerHTML = currentTitle;
        this.editInput.value = div.textContent;
        this.editModal.classList.remove('hidden');
        this.editModal.classList.add('flex');
        this.editInput.focus();
    }

    /**
     * 수정 모달 닫기
     */
    closeEditModal() {
        this.editingId = null;
        this.editInput.value = '';
        this.editModal.classList.add('hidden');
        this.editModal.classList.remove('flex');
    }

    /**
     * 수정 제출 처리
     */
    handleEditSubmit(e) {
        e.preventDefault();

        const newTitle = this.editInput.value.trim();

        if (!newTitle) {
            alert('버킷 리스트 내용을 입력해주세요!');
            return;
        }

        if (this.editingId) {
            BucketStorage.updateItem(this.editingId, newTitle);
            this.closeEditModal();
            this.render();
        }
    }

    /**
     * 삭제 처리
     */
    handleDelete(id, title) {
        if (confirm(`"${title}"\n정말 삭제하시겠습니까?`)) {
            BucketStorage.deleteItem(id);
            this.render();
        }
    }

    /**
     * 위치 검색
     */
    getSelectedUni() {
        if (!this.selectedId) return null;
        const item = BucketStorage.load().find(i => i.id === this.selectedId);
        if (!item) return null;
        const parts = item.title.split('||');
        return { uni: parts[0] || '', dept: parts[1] || '' };
    }

    handleSelect(id) {
        this.selectedId = (this.selectedId === id) ? null : id;
        this.admissionSection.classList.add('hidden');
        this.mapSection.classList.add('hidden');
        this.render();
        const info = this.getSelectedUni();
        if (info) {
            this.selectedLabel.innerHTML = `✅ <b>${this.escapeHtml(info.uni)}</b>${info.dept ? ` · ${this.escapeHtml(info.dept)}` : ''} 선택됨`;
            this.selectedLabel.className = 'mt-3 pt-3 border-t border-slate-100 text-center text-xs font-bold text-violet-700 bg-violet-50 -mx-4 -mb-4 px-4 pb-4 rounded-b-2xl';
        } else {
            this.selectedLabel.textContent = '👆 위 목록에서 대학을 탭하면 정보를 확인할 수 있어요';
            this.selectedLabel.className = 'mt-3 pt-3 border-t border-slate-100 text-center text-xs text-slate-400';
        }
    }

    handleLocationSearch() {
        const info = this.getSelectedUni();
        const query = info ? info.uni : this.uniInput.value.trim();
        if (!query) {
            alert('목록에서 대학을 먼저 선택해주세요!');
            return;
        }
        const encoded = encodeURIComponent(query);
        this.mapFrame.src = `https://maps.google.com/maps?q=${encoded}&output=embed&hl=ko`;
        this.mapTitle.textContent = `📍 ${query} 위치`;
        this.mapSection.classList.remove('hidden');
        setTimeout(() => this.mapSection.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
    }

    findUniUrl(uni) {
        if (UNI_MAIN_URL[uni]) return UNI_MAIN_URL[uni];
        for (const [key, url] of Object.entries(UNI_MAIN_URL)) {
            if (uni.includes(key) || key.includes(uni)) return url;
        }
        return null;
    }

    findDeptUrl(uni, dept) {
        const depts = DEPT_URL_MAP[uni];
        if (!depts) return null;
        if (depts[dept]) return depts[dept];
        for (const [key, url] of Object.entries(depts)) {
            if (dept.includes(key) || key.includes(dept)) return url;
        }
        return null;
    }

    handleHomepage() {
        const info = this.getSelectedUni();
        if (!info) { alert('목록에서 대학을 먼저 선택해주세요!'); return; }

        const popupOpts = 'width=1024,height=768,scrollbars=yes,resizable=yes';

        // 1순위: 학과 홈페이지 직접 URL
        if (info.dept) {
            const deptUrl = this.findDeptUrl(info.uni, info.dept);
            if (deptUrl) {
                window.open(deptUrl, 'homepagePopup', popupOpts);
                return;
            }
        }

        // 2순위: 대학 메인 홈페이지 직접 URL
        const uniUrl = this.findUniUrl(info.uni);
        if (uniUrl) {
            window.open(uniUrl, 'homepagePopup', popupOpts);
            return;
        }

        // 3순위: 네이버 검색 (미등록 대학)
        const q = encodeURIComponent(info.uni + (info.dept ? ' ' + info.dept : '') + ' 홈페이지');
        window.open(`https://search.naver.com/search.naver?query=${q}`, 'homepagePopup', popupOpts);
    }

    findSubjectData(dept) {
        const d = dept.toLowerCase();
        return SUBJECT_DATA.find(s => s.keywords.some(k => d.includes(k.toLowerCase()) || k.toLowerCase().includes(d))) || null;
    }

    findCsatMin(uni) {
        if (UNI_CSAT_MIN[uni]) return UNI_CSAT_MIN[uni];
        for (const [key, val] of Object.entries(UNI_CSAT_MIN)) {
            if (uni.includes(key) || key.includes(uni)) return val;
        }
        return null;
    }

    _csatBadge(text, planUrl) {
        const label = '<span class="text-slate-400">수능최저 : </span>';
        if (text === null || text === undefined) {
            const link = planUrl
                ? `<a href="${planUrl}" target="_blank" class="text-indigo-500 underline">시행계획 PDF 확인</a>`
                : '시행계획 확인 필요';
            return `<p class="mt-1">${label}<span class="text-slate-400">📄 ${link}</span></p>`;
        }
        return `<p class="mt-1">${label}<span class="text-slate-700 font-semibold">${this.escapeHtml(text)}</span></p>`;
    }

    renderSubjectTable(info, sd) {
        const dept = this.escapeHtml(info.dept);
        const csat = this.findCsatMin(info.uni);
        const planUrl = this.findUrlInTable(UNI_PLAN_URL, info.uni);

        const 교과Csat = csat ? csat.교과 : null;
        const 종합Csat = csat ? csat.종합 : null;

        if (!sd) {
            this.subjectTableSection.innerHTML = `
                <div class="rounded-xl overflow-hidden border border-slate-200 text-xs">
                    <div class="bg-slate-100 px-3 py-2 font-bold text-slate-500">📚 ${dept} — 2028 전형별 수능최저</div>
                    <div class="grid grid-cols-[72px_1fr]">
                        <div class="bg-indigo-50 px-2 py-3 font-bold text-indigo-700 flex items-center justify-center border-t border-slate-200 text-center leading-tight">교과<br>전형</div>
                        <div class="p-3 border-l border-t border-slate-200">
                            <p class="text-slate-400">계열 과목 데이터 없음</p>
                            ${this._csatBadge(교과Csat, planUrl)}
                        </div>
                    </div>
                    <div class="grid grid-cols-[72px_1fr]">
                        <div class="bg-violet-50 px-2 py-3 font-bold text-violet-700 flex items-center justify-center border-t border-slate-200 text-center leading-tight">종합<br>전형</div>
                        <div class="p-3 border-l border-t border-slate-200">
                            <p class="text-slate-400">계열 과목 데이터 없음</p>
                            ${this._csatBadge(종합Csat, planUrl)}
                        </div>
                    </div>
                </div>`;
            return;
        }

        const tagClass = 'inline-block bg-white border border-slate-200 text-slate-700 px-2 py-0.5 rounded-full font-semibold';
        const 교과Tags = sd.교과.과목.map(s => `<span class="${tagClass}">${s}</span>`).join('');
        const 종합Tags = sd.종합.권장과목.map(s => `<span class="${tagClass}">${s}</span>`).join('');

        this.subjectTableSection.innerHTML = `
        <div class="rounded-xl overflow-hidden border border-slate-200 text-xs">
            <div class="bg-slate-100 px-3 py-2 font-bold text-slate-600 flex items-center gap-1.5">
                📚 <span>${this.escapeHtml(sd.label)}</span>
                <span class="ml-auto text-slate-400 font-normal">2028 기준</span>
            </div>
            <div class="grid grid-cols-[72px_1fr]">
                <div class="bg-indigo-50 px-2 py-3 font-bold text-indigo-700 flex items-center justify-center border-t border-slate-200 text-center leading-tight">교과<br>전형</div>
                <div class="p-3 border-l border-t border-slate-200 space-y-1.5">
                    <p class="text-slate-500 font-semibold" style="font-size:0.65rem">주요 반영 과목</p>
                    <div class="flex flex-wrap gap-1">${교과Tags}</div>
                    ${this._csatBadge(교과Csat, planUrl)}
                </div>
            </div>
            <div class="grid grid-cols-[72px_1fr]">
                <div class="bg-violet-50 px-2 py-3 font-bold text-violet-700 flex items-center justify-center border-t border-slate-200 text-center leading-tight">종합<br>전형</div>
                <div class="p-3 border-l border-t border-slate-200 space-y-1.5">
                    <p class="text-slate-500 font-semibold" style="font-size:0.65rem">권장 이수 과목</p>
                    <div class="flex flex-wrap gap-1">${종합Tags}</div>
                    <p class="text-slate-500 leading-relaxed">${this.escapeHtml(sd.종합.역량)}</p>
                    ${this._csatBadge(종합Csat, planUrl)}
                </div>
            </div>
        </div>`;
    }

    findUrlInTable(table, uni) {
        if (table[uni]) return table[uni];
        for (const [key, url] of Object.entries(table)) {
            if (uni.includes(key) || key.includes(uni)) return url;
        }
        return null;
    }

    handleAdmission() {
        const info = this.getSelectedUni();
        if (!info) { alert('목록에서 대학을 먼저 선택해주세요!'); return; }

        // 학과별 2028 주요 과목 테이블
        const sd = this.findSubjectData(info.dept);
        this.renderSubjectTable(info, sd);

        // 시행계획 PDF 링크 (경기진협 나침반)
        const planUrl = this.findUrlInTable(UNI_PLAN_URL, info.uni);
        if (planUrl) {
            this._planPopupUrl = planUrl;
            this.uniPlanLink.textContent = `📄 ${info.uni} 2028 시행계획 PDF`;
            this.uniPlanLinkWrap.classList.remove('hidden');
        } else {
            this._planPopupUrl = null;
            this.uniPlanLinkWrap.classList.add('hidden');
        }

        // 입학처 홈페이지 링크
        const admUrl = this.findUrlInTable(UNI_ADMISSION_URL, info.uni);
        if (admUrl) {
            this.uniAdmLink.href = admUrl;
            this.uniAdmLink.textContent = `🎓 ${info.uni} 입학처 홈페이지`;
            this.uniAdmLinkWrap.classList.remove('hidden');
        } else {
            this.uniAdmLinkWrap.classList.add('hidden');
        }

        this.admissionSection.classList.remove('hidden');
        setTimeout(() => this.admissionSection.scrollIntoView({ behavior: 'smooth', block: 'start' }), 100);
    }

    handleGrade() {
        const info = this.getSelectedUni();
        if (!info) { alert('목록에서 대학을 먼저 선택해주세요!'); return; }

        this.gradeModalLabel.textContent = `${info.uni} ${info.dept}`;
        this.gradeInput.value = '';
        // 5등급제로 초기화
        document.querySelectorAll('input[name="gradeSystem"]').forEach(r => {
            r.checked = (r.value === '5');
        });
        this.gradeInput.max = '5';
        this.gradeInput.placeholder = '예) 2.5';
        this.gradeInputHint.textContent = '1~5 등급 입력 (소수점 가능)';

        this.gradeModal.classList.remove('hidden');
        this.gradeModal.classList.add('flex');
        setTimeout(() => this.gradeInput.focus(), 50);
    }

    closeGradeModal() {
        this.gradeModal.classList.add('hidden');
        this.gradeModal.classList.remove('flex');
    }

    async submitGradeCheck() {
        const gradeStr = this.gradeInput.value.trim();
        const userGrade = parseFloat(gradeStr);
        const system = document.querySelector('input[name="gradeSystem"]:checked')?.value || '5';
        const maxGrade = system === '9' ? 9 : 5;

        if (!gradeStr || isNaN(userGrade) || userGrade < 1 || userGrade > maxGrade) {
            alert(`1~${maxGrade} 사이의 등급을 입력해주세요.`);
            return;
        }

        const info = this.getSelectedUni();
        this.closeGradeModal();

        const grade9 = system === '5' ? this.convert5to9(userGrade) : userGrade;
        const grade5 = this.convert9to5(grade9);

        // 로딩 표시 후 Gemini 조회
        this.showGradeLoading(info);

        const apiKey = localStorage.getItem('geminiApiKey');
        let cutoff = null;

        if (apiKey) {
            cutoff = await this.fetchGeminiCutoff(info.uni, info.dept);
        }

        // Gemini 결과 없으면 정적 데이터 fallback
        if (!cutoff) {
            cutoff = this.findCutoff(info.uni, info.dept);
        }

        this.showGradeResult(info, grade9, grade5, userGrade, system, cutoff);
    }

    showGradeLoading(info) {
        this.gradeResultCard.style.borderColor = '#e2e8f0';
        this.gradeResultIcon.textContent = '🔍';
        this.gradeResultTitle.textContent = 'Gemini에서 입결 조회 중...';
        this.gradeResultTitle.className = 'text-base font-bold text-center mb-3 text-slate-400';
        this.gradeResultContent.innerHTML = `
            <p class="text-xs text-center text-slate-500 mb-4">${this.escapeHtml(info.uni)} · ${this.escapeHtml(info.dept)}</p>
            <div class="flex justify-center py-4">
                <div class="w-10 h-10 border-4 border-violet-100 border-t-violet-500 rounded-full animate-spin"></div>
            </div>
        `;
        this.gradeResultModal.classList.remove('hidden');
        this.gradeResultModal.classList.add('flex');
    }

    async fetchGeminiCutoff(uni, dept) {
        const apiKey = localStorage.getItem('geminiApiKey');
        if (!apiKey) return null;

        const prompt = `${uni} ${dept}의 최근 수시 교과전형(학생부교과) 합격자 내신 평균 등급을 알려주세요. 9등급제 기준 숫자만 답하세요 (예: 2.5). 모르면 "없음"이라고만 답하세요.`;

        try {
            const res = await fetch(
                `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`,
                {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        contents: [{ parts: [{ text: prompt }] }],
                        generationConfig: { temperature: 0.1, maxOutputTokens: 50 }
                    })
                }
            );

            if (!res.ok) {
                const err = await res.json();
                console.warn('Gemini API 오류:', err.error?.message);
                return null;
            }

            const data = await res.json();
            const text = (data.candidates?.[0]?.content?.parts?.[0]?.text || '').trim();

            if (/없음|모름|알 수 없|정보 없|확인 불/.test(text)) {
                return null;
            }

            const match = text.match(/(\d+\.?\d*)/);
            if (!match) return null;
            const grade = parseFloat(match[1]);
            if (grade < 1 || grade > 9) return null;

            return { grade9: grade, label: `Gemini 조회 결과 — ${grade}등급 (참고용)` };
        } catch (e) {
            console.warn('Gemini 조회 실패:', e.message);
            return null;
        }
    }

    openApiKeyModal() {
        const stored = localStorage.getItem('geminiApiKey') || '';
        this.apiKeyInput.value = stored;
        this.apiKeyModal.classList.remove('hidden');
        this.apiKeyModal.classList.add('flex');
        setTimeout(() => this.apiKeyInput.focus(), 50);
    }

    closeApiKeyModal() {
        this.apiKeyModal.classList.add('hidden');
        this.apiKeyModal.classList.remove('flex');
    }

    saveApiKey() {
        const key = this.apiKeyInput.value.trim();
        if (!key) { alert('API 키를 입력해주세요.'); return; }
        localStorage.setItem('geminiApiKey', key);
        this.closeApiKeyModal();
        alert('API 키가 저장되었습니다. 이제 입결을 자동으로 조회합니다.');
    }

    convert9to5(grade9) {
        // 9등급(1~9) → 5등급(1~5) 선형 보간: g5 = 1 + (g9-1) * 0.5
        const g5 = 1 + (grade9 - 1) * 0.5;
        return Math.round(g5 * 100) / 100;
    }

    convert5to9(grade5) {
        // 5등급(1~5) → 9등급(1~9) 선형 보간: g9 = 1 + (g5-1) * 2
        const g9 = 1 + (grade5 - 1) * 2;
        return Math.round(g9 * 100) / 100;
    }

    findCutoff(uni, dept) {
        let uniData = CUTOFF_DATA[uni];
        if (!uniData) {
            for (const [key, data] of Object.entries(CUTOFF_DATA)) {
                if (uni.includes(key) || key.includes(uni)) { uniData = data; break; }
            }
        }
        if (!uniData) return null;
        if (uniData[dept]) return uniData[dept];
        for (const [key, val] of Object.entries(uniData)) {
            if (dept.includes(key) || key.includes(dept)) return val;
        }
        return null;
    }

    showGradeResult(info, grade9, grade5, inputGrade, system, cutoff) {
        const uniDept = this.escapeHtml(`${info.uni} ${info.dept}`);
        const searchQ = encodeURIComponent(`${info.uni} ${info.dept} 2026 교과전형 합격 등급 입결`);
        const searchLink = `<a href="https://search.naver.com/search.naver?query=${searchQ}" target="_blank"
            class="flex items-center gap-2 px-3 py-2 bg-indigo-50 rounded-xl text-indigo-600 text-xs font-semibold hover:bg-indigo-100 transition-colors">
            🔍 ${uniDept} 교과전형 입결 검색
        </a>`;
        const disclaimer = `<p class="text-xs text-slate-400">※ 2026학년도 수시 교과전형 70%컷 기준 참고값입니다. 실제 입결과 다를 수 있습니다.</p>`;

        if (!cutoff) {
            this.gradeResultCard.style.borderColor = '#e2e8f0';
            this.gradeResultIcon.textContent = '🔍';
            this.gradeResultTitle.textContent = '입결 데이터 없음';
            this.gradeResultTitle.className = 'text-base font-bold text-center mb-3 text-slate-700';
            this.gradeResultContent.innerHTML = `
                <p class="text-xs font-bold text-slate-700 mb-2">${uniDept}</p>
                ${this._buildTable({
                    borderColor: 'border-slate-200',
                    headerBg: 'bg-slate-100',
                    rowBg: 'bg-slate-50',
                    my9: grade9, my5: grade5,
                    cut9: null, cut5: null
                })}
                <p class="text-xs text-slate-500">해당 대학/학과의 입결 데이터가 없습니다.</p>
                ${searchLink}
                ${disclaimer}
            `;
        } else {
            const cutoff9 = cutoff.grade9;
            const cutoff5 = this.convert9to5(cutoff9);
            const isPassing = grade9 <= cutoff9;

            this.gradeResultCard.style.borderColor = isPassing ? '#86efac' : '#fca5a5';
            this.gradeResultIcon.textContent = isPassing ? '🎉' : '📚';
            this.gradeResultTitle.textContent = isPassing ? '합격 가능성 있습니다!' : '다른 대학을 생각해보세요';
            this.gradeResultTitle.className = `text-base font-bold text-center mb-3 ${isPassing ? 'text-green-600' : 'text-red-500'}`;

            const colors = isPassing
                ? { borderColor: 'border-green-200', headerBg: 'bg-green-100', rowBg: 'bg-green-50' }
                : { borderColor: 'border-red-200',   headerBg: 'bg-red-100',   rowBg: 'bg-red-50'   };

            this.gradeResultContent.innerHTML = `
                <p class="text-xs font-bold text-slate-700 mb-1">${uniDept}</p>
                <p class="text-xs text-slate-400 mb-2">${this.escapeHtml(cutoff.label)}</p>
                ${this._buildTable({ ...colors, my9: grade9, my5: grade5, cut9: cutoff9, cut5: cutoff5 })}
                ${searchLink}
                ${disclaimer}
            `;
        }

        this.gradeResultModal.classList.remove('hidden');
        this.gradeResultModal.classList.add('flex');
    }

    _buildTable({ borderColor, headerBg, rowBg, my9, my5, cut9, cut5 }) {
        const b = borderColor;

        // 9등급 차이 계산
        let diff9Text = '—', diff9Color = 'text-slate-400';
        if (cut9 !== null) {
            const d = parseFloat((cut9 - my9).toFixed(1));
            if (d > 0.04)       { diff9Text = `${d.toFixed(1)}등급 유리`;  diff9Color = 'text-green-600'; }
            else if (d < -0.04) { diff9Text = `${Math.abs(d).toFixed(1)}등급 불리`; diff9Color = 'text-red-500'; }
            else                { diff9Text = '동등';                        diff9Color = 'text-amber-500'; }
        }

        // 5등급 차이 계산
        let diff5Text = '—', diff5Color = 'text-slate-400';
        if (cut5 !== null) {
            const d5 = cut5 - my5;
            if (d5 > 0)      { diff5Text = `${d5}등급 유리`;  diff5Color = 'text-green-600'; }
            else if (d5 < 0) { diff5Text = `${Math.abs(d5)}등급 불리`; diff5Color = 'text-red-500'; }
            else             { diff5Text = '동등';              diff5Color = 'text-amber-500'; }
        }

        const cut9Cell = cut9 !== null ? `<b>${cut9}</b>등급` : '<span class="text-slate-400">—</span>';
        const cut5Cell = cut5 !== null ? `<b>${cut5}</b>등급` : '<span class="text-slate-400">—</span>';

        return `
        <div class="rounded-xl overflow-hidden border ${b} text-xs mb-2">
            <div class="grid grid-cols-3 ${headerBg} font-bold text-slate-600 text-center">
                <div class="py-2 px-2 text-left text-slate-500">구분</div>
                <div class="py-2 border-l ${b}">5등급제</div>
                <div class="py-2 border-l ${b}">9등급제</div>
            </div>
            <div class="grid grid-cols-3 border-t ${b} bg-white">
                <div class="py-2.5 px-2 font-semibold text-slate-500">나의 등급</div>
                <div class="py-2.5 border-l ${b} text-center font-bold text-violet-600"><b>${my5}</b>등급</div>
                <div class="py-2.5 border-l ${b} text-center font-bold text-violet-600"><b>${my9}</b>등급</div>
            </div>
            <div class="grid grid-cols-3 border-t ${b} bg-white">
                <div class="py-2.5 px-2 font-semibold text-slate-500">2026<br><span class="text-slate-400 font-normal" style="font-size:0.6rem">평균 합격선</span></div>
                <div class="py-2.5 border-l ${b} text-center font-bold text-slate-700">${cut5Cell}</div>
                <div class="py-2.5 border-l ${b} text-center font-bold text-slate-700">${cut9Cell}</div>
            </div>
            <div class="grid grid-cols-3 border-t ${b} ${rowBg}">
                <div class="py-2.5 px-2 font-semibold text-slate-500">차이</div>
                <div class="py-2.5 border-l ${b} text-center font-bold ${diff5Color}">${diff5Text}</div>
                <div class="py-2.5 border-l ${b} text-center font-bold ${diff9Color}">${diff9Text}</div>
            </div>
        </div>`;
    }

    updateStats() {}

    /**
     * 대학 목록 항목 HTML 생성
     */
    createBucketItemHTML(item) {
        const parts = item.title.split('||');
        const uni = this.escapeHtml(parts[0] || item.title);
        const dept = this.escapeHtml(parts[1] || '');
        const safeTitleAttr = this.escapeHtml(item.title).replace(/'/g, '&#39;');

        const date = new Date(item.createdAt).toLocaleDateString('ko-KR', { month: 'long', day: 'numeric' });
        const completedDate = item.completedAt
            ? new Date(item.completedAt).toLocaleDateString('ko-KR', { month: 'long', day: 'numeric' })
            : null;

        const isSelected = item.id === this.selectedId;
        const selectedClass = isSelected ? 'selected' : '';

        const selectBtn = `
            <label class="flex-shrink-0 flex items-center gap-1 cursor-pointer select-none py-0.5"
                   onclick="event.stopPropagation()" title="체크하면 정보를 확인할 수 있어요">
                <input type="checkbox" class="uni-checkbox" ${isSelected ? 'checked' : ''}
                       onchange="app.handleSelect('${item.id}')">
                <span class="text-[10px] font-bold ${isSelected ? 'text-violet-600' : 'text-slate-400'}">${isSelected ? '선택됨' : '선택'}</span>
            </label>`;

        return `
            <div class="bucket-item ${selectedClass} bg-white rounded-xl p-2.5 flex items-center gap-3 shadow-sm border border-slate-100 hover:shadow-md transition-all cursor-pointer"
                 data-id="${item.id}" onclick="app.handleSelect('${item.id}')">
                ${selectBtn}
                <div class="flex-1 min-w-0">
                    <p class="text-xs font-semibold text-slate-800 truncate">
                        ${uni}${dept ? `<span class="text-violet-500 font-medium"> · ${dept}</span>` : ''}
                        <span class="text-slate-400 font-normal" style="font-size:0.65rem"> · ${date} 추가</span>
                    </p>
                </div>
                <div class="flex gap-1.5 flex-shrink-0" onclick="event.stopPropagation()">
                    <button
                        onclick="app.handleDelete('${item.id}', '${safeTitleAttr}')"
                        title="삭제"
                        class="delete-btn w-8 h-8 rounded-full flex items-center justify-center transition-all hover:scale-110">
                        <svg viewBox="0 0 24 24" fill="currentColor" class="w-4 h-4">
                            <path d="M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z"/>
                        </svg>
                    </button>
                </div>
            </div>
        `;
    }

    /**
     * HTML 이스케이프 처리
     */
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * 화면 렌더링
     */
    render() {
        // 통계 업데이트
        this.updateStats();

        // 필터링된 리스트 가져오기
        const bucketList = BucketStorage.getFilteredList(this.currentFilter);

        // 리스트가 비어있으면 빈 상태 표시
        if (bucketList.length === 0) {
            this.bucketListContainer.innerHTML = '';
            this.emptyState.classList.remove('hidden');
            this.listHint.classList.add('hidden');
            this.listHint.classList.remove('flex');
            return;
        }

        // 빈 상태 숨기기
        this.emptyState.classList.add('hidden');
        this.listHint.classList.remove('hidden');
        this.listHint.classList.add('flex');

        // 리스트 렌더링
        const html = bucketList.map(item => this.createBucketItemHTML(item)).join('');
        this.bucketListContainer.innerHTML = html;
    }
}

// 앱 인스턴스 생성
let app;
document.addEventListener('DOMContentLoaded', () => {
    app = new BucketListApp();
});
