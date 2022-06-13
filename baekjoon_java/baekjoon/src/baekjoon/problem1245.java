package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem1245 {
	static int N;
	static int M;
	static int[] dx = {1,0,-1,0,1,1,-1,-1};
	static int[] dy = {0,1,0,-1,-1,1,-1,1};
	static int max;
	static int[][] map;
	static boolean[][] visited;
	static boolean flag;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		map = new int[N][M];
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}
		visited=new boolean[N][M];
		max=0;
		int cnt=0;

		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(!visited[i][j] && map[i][j]!=0) {	
					flag=true;
					DFS(i,j);
//					System.out.println(i+" "+j);
					if(flag)
						cnt++;
				}
			}
		}
		
		System.out.println(cnt);
	}
	static void DFS(int x, int y) {
		visited[x][y]=true;
		for(int i=0; i<8; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if(0<=nx && nx<N && 0<=ny && ny<M ) {
				if(map[nx][ny]>map[x][y]) {
					flag=false;
				}
				if(!visited[nx][ny] && map[nx][ny]==map[x][y]) {
					DFS(nx,ny);
				}
			}
		}
	}

}
