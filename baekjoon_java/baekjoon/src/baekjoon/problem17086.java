package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem17086 {
	
	static int[] dx = {-1,-1,0,1,1,1,0,-1};
	static int[] dy = {0,1,1,1,0,-1,-1,-1};
	static int N;
	static int M;
	static int map[][];
	static int copy[][];
	static int max = Integer.MIN_VALUE;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		map = new int[N][M];
		copy = new int[N][M];
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(map[i][j] == 1) {
					BFS(i,j);
				}
			}
		}
		System.out.println(max);
	}

	
	static void BFS(int x,int y) {
		
		
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] {x,y});
		
		while (!q.isEmpty()) {

			int[] temp = q.poll();

			for (int i = 0; i < 8; i++) {
				int nx = temp[0] + dx[i];
				int ny = temp[1] + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < M) {
					if (copy[nx][ny] != 0 || map[nx][ny] == 1) {
						continue;
					} 
					copy[nx][ny] = copy[x][y] + 1;
					q.add(new int[] { nx, ny });
					max = Math.max(max, copy[nx][ny]);
					
				}
			}

		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				System.out.print(copy[i][j]+" ");
			}
			System.out.println();
		}
		System.out.println();
		return ;
	}
}
