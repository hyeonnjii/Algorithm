# [Silver IV] 요세푸스 문제 - 1158 

[문제 링크](https://www.acmicpc.net/problem/1158) 

### 성능 요약

메모리: 34008 KB, 시간: 68 ms

### 제출 일자

2023년 12월 22일 21:58:59

### 문제 설명

<p>요세푸스 문제는 다음과 같다.</p>

<p>1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.</p>

<p>N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)</p>

### 출력 
 
 <p>예제와 같이 요세푸스 순열을 출력한다.</p>
 
----------------------------------------------------------------------

### 구현 로직

<ul>
  <li>
    '큐' 알고리즘을 사용하여 구현
  </li>
  <li>
    collections의 deque 라이브러리를 사용
  </li>
  <li>
    'rotate(-(k-1))' : k-1 만큼 회전 후 popleft() 수행
  </li>
</ul>

<p>해당 큐를 사용한 요세푸스 시간복잡도는 O(n*k)</p>
<ol>
 <li>
  시계방향으로 k만큼 이동하는 횟수가 n-1회이므로 O(N) 소요
 </li>
 <li>
  rotate 되는 동안, popleft(=O(1))와 append(=O(1)) 되므로 O(K)(=O(K-1)) 소요 
 </li>
 <li>
  * Ref. rotate(-(k-1)): 원소를 왼쪽으로 k-1 번 회전 = k-1 번째 원소가 맨 뒤로 가게 됨
  * ex) 1 2 3 4  -> (4, 2) -> 2 3 4 1 
 </li>
</ol>

---------------------------------------------------------------------

### 결론 
<p>O(nk) 시간복잡도를 가짐</p>

--------------------------------------------------------------------
Reference) https://measurezero.tistory.com/1193

### [요세푸스 문제]

#### 알고리즘

#### 1. O(nk) 해법

<li>가장 단순한 풀이 중 하나로 '큐(queue)' 자료구조</li>

#### 2. O(nlgn) 해법

<li>위 방법보다 조금 더 빠른 풀이로 '세그먼트트리'를 이용</li>



