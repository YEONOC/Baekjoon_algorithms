# [벌집](https://www.acmicpc.net/problem/2292)



# 문제

<img width="300" src="https://www.acmicpc.net/JudgeOnline/upload/201009/3(2).png"/>

위의 그림과 같이 육각형으로 이루어진 벌집이 있다. 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

---

# 입력

첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

---

# 출력

입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.

---


# 예제 입력 1

    13

---

# 예제 출력 1

    3

---
# 출처

ICPC > Regionals > Asia Pacific > Korea > Nationwide Internet Competition > Seoul Nationalwide Internet Competition 2004 B번

 - 문제의 오타를 찾은 사람: waylight3

---

# 문제 접근
  
  - 벌집 그림에 관한 규칙을 찾음.

  - n이 2 이상일 때 n이 a보다 크고 a+6*i보다 작으면 1부터 n까지의 벌집 칸은 i+1칸임을 출력

  - a는 2부터 시작하고 while문을 통해 a= a+6*i를 늘려가고 i를 1씩 늘림