package baekjoon;

import java.util.*;
import java.io.*;

public class problem2583 {
	
	static int N;
	static int M;
	static int K;
	static int[][] map;
	static boolean[][] visited;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,1,-1};
	static int cnt;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		N=Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		K = Integer.parseInt(str[2]);
		map= new int[N][M];
		for(int t=0; t<K; t++) {
			str = br.readLine().split(" ");
			int[][] temp = new int[2][2];
			temp[0][0]=Integer.parseInt(str[0]);
			temp[0][1]=Integer.parseInt(str[1]);
			temp[1][0]=Integer.parseInt(str[2]);
			temp[1][1]=Integer.parseInt(str[3]);
			for(int i=temp[0][1]; i<temp[1][1]; i++) {
				for(int j=temp[0][0]; j<temp[1][0]; j++) {
					map[i][j]=-1;
				}
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				System.out.print(map[i][j]+" ");
			}
			System.out.println();
		}
		ArrayList<Integer> z = new ArrayList<Integer>();
		visited= new boolean[N][M];
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(!visited[i][j]&&map[i][j]!=-1) {
					cnt=1;
					DFS(i,j);
					z.add(cnt);
				}
			}
		}
		Collections.sort(z);
		int size = z.size();
		System.out.println(size);
		for(int i=0; i<size; i++) {
			System.out.print(z.get(i)+" ");
		}
	}
	
	static void DFS(int x, int y) {
		visited[x][y] = true;
		for(int i=0; i<4; i++) {
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(0<=nx && nx<N && 0<=ny && ny<M && !visited[nx][ny] && map[nx][ny]!=-1) {
				DFS(nx,ny);
				cnt++;
			}
		}
	}

}
