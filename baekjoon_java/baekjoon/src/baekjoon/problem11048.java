package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem11048 {
	static int dx[] = {1,0};
	static int dy[] = {0,1};
	
	static int N;
	static int M;
	static int[][] room;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str[] = br.readLine().split(" ");
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		
		room = new int[N][M];
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			for(int j=0; j<M; j++) {
				room[i][j] = Integer.parseInt(str[j]); 
			}
		}
		BFS(0,0);
	}
	static void BFS(int x,int y) {
		Queue<int[]> q = new LinkedList<int[]>();
		boolean visited[][] = new boolean[N][M];
		q.offer(new int[] {x,y});
		int[][] copy= new int[N][M];
		copy[x][y]=room[x][y];
		visited[x][y] = true;
		while(!q.isEmpty()) {
			int[] temp = q.poll();
			for(int i=0; i<2; i++) {
				int nx = temp[0]+ dx[i];
				int ny = temp[1] + dy[i];
				if(nx>=0 && nx<N && ny>=0 &&ny<M) {
					if(!visited[nx][ny]) {
						copy[nx][ny]=room[nx][ny]+copy[temp[0]][temp[1]];
						q.offer(new int[] {nx,ny});
						visited[nx][ny]=true;
					}
					else if(room[nx][ny]+copy[temp[0]][temp[1]]>copy[nx][ny]) {
						q.offer(new int[] {nx,ny});
						copy[nx][ny]=room[nx][ny]+copy[temp[0]][temp[1]];
					}
				}
			}
		}
		System.out.println(copy[N-1][M-1]);
		return;
	}
}
