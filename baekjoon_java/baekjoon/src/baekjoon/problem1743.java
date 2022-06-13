package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem1743 {
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static int N;
	static int M;
	static int K;
	static int map[][];
	static boolean visited[][];
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		N = Integer.parseInt(str[0])+1;
		M = Integer.parseInt(str[1])+1;
		K = Integer.parseInt(str[2]);
		map = new int[N][M];
		visited = new boolean [N][M];
		for(int i=0; i<K; i++) {
			str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			
			map[a][b] = 1;
		}
		int max = Integer.MIN_VALUE;
		for(int i=1; i<N; i++) {
			for(int j=1; j<M; j++) {
				if(map[i][j] == 1 && !visited[i][j]) {
//					System.out.println(i+" "+j);
					max = Math.max(max, BFS(i,j));
				}
			}
		}
		System.out.println(max);
	}
	static int BFS(int x, int y) {
		int cnt =1;
		Queue<int[]> q = new LinkedList<int[]>();
		q.offer(new int[] {x,y});
		visited[x][y]=true;
//		System.out.println("test");
		while(!q.isEmpty()) {
			int[] temp = q.poll();
			for(int i=0; i<4; i++) {
				int nx = temp[0]+dx[i];
				int ny = temp[1]+dy[i];
				if(0<nx&&nx<N &&0<ny && ny<M&&!visited[nx][ny] && map[nx][ny]==1) {
//					System.out.println(nx+" "+ny);
					cnt++;
					visited[nx][ny] = true;
					q.offer(new int[] {nx,ny});
				}
			}
		}
		
		return cnt;
	}
}
