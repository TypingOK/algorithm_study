package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem2636 {
	static int N;
	static int M;
	static int[][] map;
	static int[][] copy;
	static boolean[][] visited;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	
	public static void main(String[] args) throws IOException{ 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str[] = br.readLine().split(" ");
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		
		map=new int[N][M];
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}
		for (int j = 0; j < M; j++) {
			map[0][j] = 2;
		}
		for (int j = 0; j < N; j++) {
			map[j][0] = 2;
		}
		for(int j=0; j<M; j++) {
			map[N-1][j] = 2;
		}
		for(int j=0; j<N; j++) {
			map[j][M-1] =2;
		}
		
		
		int hour=0;
		int count = 0;
		for(int i=0; i<N; i++) {
			hour++;
			
			int cnt=0;
			visited = new boolean[N][M];
			for(int j=0; j<M; j++) {
				if(!visited[i][j] && map[i][j]==2) {
					 cnt+=BFS(i,j);
					 
//					 for (int k = 0; k < N; k++) {
//						 for (int n = 0; n < M; n++) {
//							 System.out.print(map[k][n] + " ");
//						 }
//						 System.out.println();
//					 }
//					 System.out.println();
//					 
				}
			}
			if(cnt!=0) {
				count=cnt;
			}else {
				break;
			}
		}
		System.out.println(hour-1);
		System.out.println(count);
	}
	
	public static int BFS(int x,int y) {
		int cnt =0;
		Queue<int[]> q = new LinkedList<int[]>();
		visited[x][y] = true;
//		System.out.println("들어와 있는 좌표"+x+" "+y);
		q.offer(new int[] {x,y});
		while(!q.isEmpty()) {
			int temp[] = q.poll();
			for(int i=0; i<4; i++) {
				int nx = temp[0] + dx[i];
				int ny = temp[1] + dy[i];
				if(0<=nx && nx<N && 0<=ny  && ny<M &&!visited[nx][ny]&& (map[nx][ny]==0 || map[nx][ny]==2)) {
					visited[nx][ny] = true;
					q.offer(new int[] {nx,ny});
				}else if(0<=nx && nx<N && 0<=ny  && ny<M &&!visited[nx][ny] && map[nx][ny]==1) {
//					System.out.println(nx+" "+ ny);
					visited[nx][ny] = true;
					map[nx][ny]=0;
					cnt++;
				}
			}
		}
		
		
		return cnt;
	}
}
