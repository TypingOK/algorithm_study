package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem2589 {
	static int N;
	static int M;
	static int[] dx = {1,-1,0,0};
	static int[] dy = {0,0,-1,1};
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str[] = br.readLine().split(" ");
		N = Integer.parseInt(str[0]);
		M = Integer.parseInt(str[1]);
		char[][] map = new char[N][M];
		for(int i=0; i<N; i++) {
			map[i] = br.readLine().toCharArray();
		}
		int max = Integer.MIN_VALUE;
		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				if(map[i][j]=='L') {
					max=Math.max(max, BFS(i,j,map));
				}
			}
		}
		System.out.println(max);
		
	}

	static int BFS(int x, int y,char[][] map) {
		int count =0;
		Queue<int[]> q = new LinkedList<int[]>();
		boolean[][] visited = new boolean[N][M];
		q.offer(new int[] {x,y});
		visited[x][y] = true;
		while(!q.isEmpty()) {
			int size = q.size();
			for(int n=0; n<size; n++) {
				int[] temp = q.poll();
				for(int i=0; i<4; i++) {
					int nx = temp[0] +dx[i];
					int ny = temp[1]+dy[i];
					if(0<=nx && nx<N && 0<=ny && ny<M &&!visited[nx][ny]&& map[nx][ny]=='L') {
						visited[nx][ny]=true;
						q.offer(new int[] {nx,ny});
					}
				}
			}
			count++;
		}
		return count-1;
	}
}
