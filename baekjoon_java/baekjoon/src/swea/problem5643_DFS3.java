package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem5643_DFS3 {
	static int[][] adjMatrix,radjMatrix;
	static int N;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC =Integer.parseInt(br.readLine());
		
		for(int tc = 1; tc<=TC; tc++) {
			N = Integer.parseInt(br.readLine());
			int M = Integer.parseInt(br.readLine());
			
			//인접행렬: 0으로 자동 초기화
			adjMatrix = new int[N+1][N+1]; //학생 번호 1부터 시작하도록
			
			for(int i=1; i<=N; i++) adjMatrix[i][0] = -1;
			
			StringTokenizer st = null;
			int a,b;
			for(int i=0; i<M; i++) { //간선 정보 입력받아 인접행렬에 표시
				st = new StringTokenizer(br.readLine()," ");
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				 adjMatrix[a][b] = 1;
			}
			
			int answer = 0; // 자신의 키를 알 수 있는 학생 수
			for (int i = 1; i <= N; i++) {
				//탐색 전인 학생들만 탐색
				if(adjMatrix[i][0] == -1) {
					gtDFS(i);
				}
			}
			
			//자기보다 작은 학생수 카운트
			for(int j=1; j<=N; j++) {
				for(int i=1; i<=N; i++) {
					adjMatrix[0][j] += adjMatrix[i][j];
				}
			}
			
			for(int i=0; i<=N; i++) {
				if(adjMatrix[i][0] + adjMatrix[0][i] == N-1) ++answer;
			}
			System.out.println("#"+tc+" "+answer);
		}
	}
	static void gtDFS(int cur) {
		for(int i=1; i<=N; i++) {
			if(adjMatrix[cur][i] !=0 ) {
				if (adjMatrix[i][0] == -1)
					gtDFS(i);
				// 나보다 큰 학생이 알고있는 다른 학생과의 키 관계를 나와의 직접 관계로 매핑

				// cur < i < j ==> cur < j
				if (adjMatrix[i][0] > 0) { // i보다 큰 학생이 있다면
					for (int j = 1; j <= N; j++) {
						if (adjMatrix[i][j] == 1) {
							adjMatrix[cur][j] = 1;
						}
					}
				}

			}
		}
		int cnt = 0;
		for (int i = 1; i <= N; i++) {
			cnt += adjMatrix[cur][i];
		}
		adjMatrix[cur][0] = cnt;
	}

}
