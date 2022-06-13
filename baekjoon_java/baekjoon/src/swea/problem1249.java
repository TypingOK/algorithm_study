package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem1249 {
	
	static int N;
	static int map[][];
	static int copy[][];
	static int min;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	static boolean[][] visited;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int TC = Integer.parseInt(br.readLine());
		char str[];
		for(int tc=1; tc<=TC; tc++) {
			N = Integer.parseInt(br.readLine());
			min = Integer.MAX_VALUE;
			map = new int[N][N];
			visited = new boolean[N][N];
			copy = new int[N][N];
			
			for(int i=0; i<N; i++) {
				str = br.readLine().toCharArray();
				for(int j=0; j<N; j++) {
					map[i][j] = (int)str[j]-'0';
					copy[i][j] = Integer.MAX_VALUE;
				}
			}
			
			dfs(0,0,0);
			System.out.println("#"+tc+" " +min);
		}
	}
	
	static void dfs(int x,int y, int sum) {
		visited[x][y] = true;
		if(sum>=min) {
			return ;
		}
		if(x==N-1 && y==N-1) {
			min = Math.min(sum, min);
			return ;
		}
		
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y + dy[i];
			if (0 <= nx && nx < N && 0 <= ny && ny < N && !visited[nx][ny] && copy[nx][ny] > sum + map[nx][ny]) {
				copy[nx][ny] = sum + map[nx][ny];
				dfs(nx, ny, sum + map[nx][ny]);
				visited[nx][ny] = false;
			}
		}
	}

}



