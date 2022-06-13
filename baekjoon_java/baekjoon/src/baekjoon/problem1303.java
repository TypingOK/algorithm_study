package baekjoon;

import java.io.*;

public class problem1303 {
	static boolean[] visited;
	static int[][] map;
	static char[][] grid;
	static int[] dx = {-1,0,1,0};
	static int[] dy= {0,-1,0,1};
	static int N;
	static int M;
	static int count;
	static int B,W;
	static int resultB;
	static int resultW;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		M = Integer.parseInt(str[0]);
		N = Integer.parseInt(str[1]);
		grid = new char[N][M];
		map = new int[N][M];
		for(int i=0; i<N; i++) {
			grid[i] = br.readLine().toCharArray();
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(map[i][j]==0) {
					count=1;
					map[i][j]=1;
					dfs(i,j);
					if(grid[i][j]=='W') {
						resultW+=(count*count);
					}else {
						resultB+=(count*count);
					}
				}
			}
		}
		System.out.println(resultW+" "+resultB);
	}
	static void dfs(int x,int y) {
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(nx>=0 && nx<N && ny>=0 && ny<M && map[nx][ny]==0 && grid[nx][ny]==grid[x][y]) {
				map[nx][ny]=map[x][y]+1;
				count++;
				dfs(nx,ny);
			}
		}
	}
	

}
