# -

"이것이 취업을 위한 코딩 테스트다"를 읽고 문제를 풀고 정리한 공간입니다.

DFS는 깊이 우선 탐색으로 부르며, 그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘이다.

그래프는 노드와 간선으로 표현하며 노드는 정점이라고도 부른다.

- 크게 2가지로 표현할 수 있는데 인접 행렬과 인접 리스트로 표현한다.
  A. 인접 행렬 : 2차원 배열로 그래프의 연결 관계를 표현하는 방식 - 인접 행렬은 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이며 연결 돠지 않은 노드는 무한의 값을 넣는다.
  B. 인접 리스트 : 리스트로 그래프의 연결 관계를 표현하는 방식 -인접 리스트 방식은 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장한다.
- 두가지 방식의 차이점은 속도와 메모리 효율에서 나온다. 인접 행렬 방식은 크기가 크면 클수록 메모리 효율에서 좋지 않다. 하지만 속도는 빠르다. 인접 리스트 방식은 그와 반대다.

DFS의 구체적인 동작 과정은 다음과 같다.

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

BFS는 너비 우선 탐색으로 부른다. 동작 과정은 다음과 같다.

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

- 일반적인 경우 DFS보다 BFS가 수행시간은 빠르다.

* 정렬은 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.

- 선택 정렬 : 데이터가 무작위로 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는것. O(N\*\*2)
- 삽입 정렬 : 데이터가 거의 정렬 되어 있을 때 효율적이다. 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬 되어 있다고 가정한다. 최선의 경우 O(N)
- 퀵 정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 알고리즘. 퀵정렬의 평균 시간 복잡도는 O(NlogN) 최악의 경우는 (N \*\* 2)
- 계수 정렬 : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘. 직접 비교하는 다른 알고리즘과는 다르게 직접적으로 수를 비교하지는 않는다.