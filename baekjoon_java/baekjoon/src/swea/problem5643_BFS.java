package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class problem5643_BFS {
	
	static int[][] adjMatrix;
	static int N;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC =Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc<=TC; tc++) {
			N = Integer.parseInt(br.readLine());
			int M = Integer.parseInt(br.readLine());
			
			//인접행렬: 0으로 자동 초기화
			adjMatrix = new int[N+1][N+1]; //학생 번호 1부터 시작하도록
			
			StringTokenizer st = null;
			int a,b;
			for(int i=0; i<M; i++) { //간선 정보 입력받아 인접행렬에 표시
				st = new StringTokenizer(br.readLine()," ");
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				adjMatrix[a][b] = 1;
			}
			
			int answer = 0; // 자신의 키를 알 수 있는 학생 수
			for(int i=1; i<=N; i++) {
				if(gtBFS(i,new boolean[N+1])+ltBFS(i,new boolean[N+1]) == N-1) ++answer;
			}
			System.out.println("#"+tc+" "+answer);
		}
	}
	
	static int gtBFS(int start,boolean[] visited) {
		
		int cnt = 0;
		Queue<Integer> queue = new LinkedList<Integer>();
		visited[start] = true;
		queue.offer(start);
		
		while(!queue.isEmpty()) {
			
			int cur = queue.poll();
			
			for(int i=1; i<=N; i++) {
				if(adjMatrix[cur][i] != 0 && !visited[i]) {
					++cnt; //자신보다 큰 학생이 얼마나 있는지 확인
					visited[i] = true;
					queue.offer(i);
				}
			}
			
		}
		return cnt;
	}
	static int ltBFS(int start,boolean[] visited) {
		int cnt = 0;
		Queue<Integer> queue = new LinkedList<Integer>();
		visited[start] = true;
		queue.offer(start);
		
		while(!queue.isEmpty()) {
			
			int cur = queue.poll();
			
			for(int i=1; i<=N; i++) {
				if(adjMatrix[i][cur] != 0 && !visited[i]) { //나보다 작은 애 탐색하기
					++cnt; //자신보다 큰 학생이 얼마나 있는지 확인
					visited[i] = true;
					queue.offer(i);
				}
			}
			
		}
		
		return cnt;
		
	}
}
