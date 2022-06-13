package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem14502 {
	static int max;
	static int N;
	static int M;
	static int[][] map;
	static int[][] copy;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	
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
		max = 0;
		comb(3);
		System.out.println(max);
		
	}
	static void capture() {
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				copy[i][j] = map[i][j];
			}
		}
	}
	
	static void comb(int count) {
		if(count==0) {
			capture();
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
					if(map[i][j] == 2) {
						dfs(i,j);
					}
				}
			}
			int cnt=0;
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
//					System.out.print(copy[i][j]+" ");
					if(copy[i][j]==0) {
						cnt++;
					}
				}
//				System.out.println();
			}
//			System.out.println("----------------------------------------");
			max = Math.max(max, cnt);
			return;
		}
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(map[i][j] == 0) {
					map[i][j] =1;
					comb(count-1);
					map[i][j] = 0;
				}
			}
		}
	}
	
	static void dfs(int x, int y) {
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			
			if(0<=nx && nx<N && 0<=ny && ny<M && copy[nx][ny]==0) {
				copy[nx][ny] = 2;
				dfs(nx,ny);
			}
		}
	}

}
