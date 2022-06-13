package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class problem2573 {
	
	static int[] dx = {1,-1,0,0};
	static int []dy = {0,0,1,-1};
	static int N;
	static int M;
	static int co[][];
	static boolean visited[][];
	
	public static void main(String[] args)  throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner sc = new Scanner(System.in);
		
		
		N = sc.nextInt();
		M = sc.nextInt();
		
		int map[][] = new int[N][M];
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				map[i][j] = sc.nextInt();
			}
		}
		
		int cnt = 0;
		int year = 0;
		boolean flag = true;
		while (flag) {
			co = new int[N][M];
			visited = new boolean[N][M];
			year++;
			cnt = 0;
			check(map);
			map = update(map);
			label: for (int i = 1; i < N - 1; i++) {
				for (int j = 1; j < M - 1; j++) {
					if (map[i][j] != 0 && !visited[i][j]) {
						cnt++;
						DFS(map, i, j);
						if (cnt == 2) {
							flag = false;
							break label;
						}
					}
				}
			}
			if(cnt==0) {
				year =0;
				break;
			}
		} // while 끝
		System.out.println(year);
	}
	
	static void check(int[][] map) {
		for(int i=1; i<N-1; i++) {
			for(int j=1; j<M-1; j++) {
				if(map[i][j]>0) {
					for(int k=0; k<4; k++) {
						int nx = i+dx[k];
						int ny = j+dy[k];
						if(map[nx][ny]==0) {
							co[i][j]++;
						}
					}
				}
			}
		}
	}
	static int[][] update(int[][] map) {
		for(int i=1; i<N-1; i++) {
			for(int j=1; j<M-1; j++) {
				map[i][j] -= co[i][j];
				if(map[i][j]<0) {
					map[i][j] =0;
				}
			}
		}
		return map;
	}
	static void DFS(int[][] map, int x,int y) {
		visited[x][y] = true;
		for(int i=0; i<4; i++) {
			int nx =x+dx[i];
			int ny = y+dy[i];
			
			if(!visited[nx][ny] && map[nx][ny]!=0) {
				DFS(map,nx,ny);
			}
		}
	}
	static void BFS(int[][] map,int x, int y){
		visited[x][y] = true;
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] {x,y});
		
		while(!q.isEmpty()) {
			int[] temp = q.poll();
			
			for(int i=0; i<4; i++) {
				int nx = temp[0] + dx[i];
				int ny = temp[1] + dy[i];
				
				if(!visited[nx][ny] && map[nx][ny]!=0){
					visited[nx][ny] = true;
					q.add(new int[] {nx,ny});

				}
				
			}
		}

		
	}

}
