package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem3187 {
	static int N;
	static char[][] Map;
	static int K;
	static int V;
	static int R;
	static int C;
	static int w;
	static int s;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String[] str = br.readLine().split(" ");
		R= Integer.parseInt(str[0]);
		C= Integer.parseInt(str[1]);
		Map = new char[R][C];
		boolean[][] visited = new boolean[R][C];
		for(int i=0; i<R; i++) {
			char[] c = br.readLine().toCharArray();
			for(int j=0; j<C; j++) {
				Map[i][j] = c[j];
				if(Map[i][j]=='k') {
					K++;
				}
				else if (Map[i][j]=='v') {
					V++;
				}
			}
		}
		for(int i=0; i<R; i++) {
			for(int j=0; j<C; j++) {
				if(!visited[i][j] &&(Map[i][j]=='k' ||Map[i][j] == 'v')) {
					if(Map[i][j]=='k') {
						s=1;
						w=0;
					}else if(Map[i][j] == 'v') {
						w=1;
						s=0;
					}
					DFS(i,j,visited);
					if(w>=s) {
						K=K-s;
					}else if(w<s) {
						V=V-w;
					}
				}
			}
		}
		System.out.println(K+" "+V);
				
	}
	static void DFS(int x, int y, boolean[][] visited) {
		visited[x][y]=true;
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(!visited[nx][ny] && 0<=nx&&nx<R && 0<=ny&&ny<C && Map[nx][ny]!='#') {
				if(Map[nx][ny]=='k') {
					s++;
				}else if(Map[nx][ny]=='v') {
					w++;
				}
				DFS(nx,ny,visited);
			}
		}
	}
}
