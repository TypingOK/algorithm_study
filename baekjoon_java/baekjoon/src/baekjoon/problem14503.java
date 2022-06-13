package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem14503 {
	static int N;
	static int M;
	static int[][] visit;
	static int [][] copy;
	static int[] dx = {-1,0,1,0};
	static int[] dy = {0,1,0,-1};
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		visit = new int[N][M];
		str = br.readLine().split(" ");
		int x = Integer.parseInt(str[0]);
		int y = Integer.parseInt(str[1]);
		int d = Integer.parseInt(str[2]);
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			for(int j=0; j<M; j++) {
				visit[i][j] = Integer.parseInt(str[j]);
			}
		}
		copy = new int[N][M];
		copy[x][y] = 1;
		dfs(x,y,d,1);
	}
	
	static void dfs(int x,int y, int d, int cnt) {
		
		
		for(int i=0; i<4; i++) {
			int nd = (d+3-i)%4;
			int nx = x+dx[nd];
			int ny = y+dy[nd];
			if(0<=nx && nx <N && 0<=ny && ny<M && visit[nx][ny]!=1 && copy[nx][ny]==0) {
				cnt+=1;
				copy[nx][ny] = cnt;
				dfs(nx,ny,nd,cnt);
			}
		}
		int nd =0;
		if (d + 2 < 4) {
			nd = d + 2;
		} else {
			nd = d - 2;
		}
		int nx = x + dx[nd];
		int ny = y + dy[nd];
		if (nx == 0 || nx == N - 1 || ny == 0 || ny == M - 1 || visit[nx][ny] == 1) {
			System.out.println(cnt);
			System.exit(0);
		} else {
			dfs(nx, ny, d, cnt);
		}
	}

}
