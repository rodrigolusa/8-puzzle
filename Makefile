image:
	docker build -t ia .

bash:
	docker run -it -v ${PWD}:/ia ia bash

test:
	docker run -v ${PWD}:/ia ia pytest src