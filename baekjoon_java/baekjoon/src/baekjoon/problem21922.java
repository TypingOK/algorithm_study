package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem21922 {
	static int N;
	static int M;
	static int[][] map;
	static boolean[][] visited;
	static int[] dx= {-1,0,1,0};
	static int[] dy= {0,-1,0,1};
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		
		N=Integer.parseInt(str[0]);
		M=Integer.parseInt(str[1]);
		Queue<int[]> temp = new LinkedList<>();
		
		map=new int[N][M];
		visited = new boolean[N][M];
		
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(str[j]);
				if(map[i][j]==9) {
					temp.add(new int[] {i,j});
					visited[i][j] = true;
				}
			}
		}
		int size = temp.size();
		
		for(int i=0; i<size; i++) {
			int[] a = temp.poll();
			for(int j=0; j<4; j++) {
				DFS(a[0],a[1],j);
			}
		}
		int answer=0;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(visited[i][j]) {
					answer++;
				}
			}
		}
		System.out.println(answer);
	}
	
	static void DFS(int x, int y, int d) {
		visited[x][y] = true;
		
		
		int nx = x+dx[d];
		int ny = y+dy[d];
		if (0 <= nx && nx < N && 0 <= ny && ny < M&&map[nx][ny]!=9) {
			if (map[nx][ny] == 1) {
				if (d == 1)
					d = 3;
				else if (d == 3)
					d = 1;
			} else if (map[nx][ny] == 2) {
				if(d==0) d=2;
				else if(d==2) d=0;
			} else if (map[nx][ny] == 3) {
				if(d==0) d=3;
				else if(d==1) d=2;
				else if(d==2) d=1;
				else if(d==3) d=0;
			} else if (map[nx][ny] == 4) {
				if(d==0) d=1;
				else if(d==1) d=0;
				else if(d==2) d=3;
				else if(d==3) d=2;
			}
			
			DFS(nx,ny,d);
		}
		
	}
}
