## 패키지 사용 가이드 (How-To-Use Package)

### 명령 프롬프트 (CMD)

#### 패키지 참조 후 실행
```
> set {프로젝트 경로}/src/basic/package
> python
>>> import themepark as themepark
>>> themepark.test_open()
```

&nbsp;
#### 주의사항
 - 반드시 `명령 프롬프트(CMD)`에서만 실행할 수 있다. (Pycharm venv 환경에서는 불가)
 - `시스템 환경 변수 설정`에서 `시스템 변수`의 `PATH`에서 아래 파이썬 경로를 지정해줘야 한다.
   - {Python 설치 경로}
   - {Python 설치 경로}/Scripts

&nbsp;
### 팁 (TIPS)
 - 패키지로 인식하려면 반드시 해당 디렉토리에 `__init__.py`가 있어야 함.
 - import 뒤에 오는 경로는 상대경로를 사용할 수 없으므로 반드시 from을 활용해야 함.
 - 만약 `import *` 를 사용할 경우 해당 디렉토리의 `__init__.py`의 `__all__`에 모듈 정의 필요함.