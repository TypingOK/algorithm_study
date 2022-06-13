package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class problem1600 {
	
	static int N;
	static int M;
	static int[][] map;
//	static boolean[][][] visited;
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	static int[] jumpx = {2,1,-1,-2,-2,-1,1,2};
	static int[] jumpy = {1,2,2,1,-1,-2,-2,-1};
	static int min;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		M =Integer.parseInt(st.nextToken());
		N =Integer.parseInt(st.nextToken());
		
		map=new int[N][M];
		for(int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<M; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		min = Integer.MAX_VALUE;
		BFS(0,0,k);
		if(min==Integer.MAX_VALUE) {
			System.out.println(-1);
		}else {
			System.out.println(min);
		}
		
	}
	
	static void BFS(int x,int y,int k) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[] { x, y, k,0 });
		boolean[][][] visited=new boolean[N][M][k+1];
		visited[0][0][k] = true;
		while (!q.isEmpty()) {
			int temp[] = q.poll();
			if (temp[0] == N - 1 && temp[1] == M - 1) {
				min = Math.min(min, temp[3]);
				return;
			}
			if (temp[2] > 0) {
				for (int i = 0; i < 8; i++) {
					int nx = temp[0] + jumpx[i];
					int ny = temp[1] + jumpy[i];
					if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny][temp[2] - 1] && map[nx][ny] == 0) {
						visited[nx][ny][temp[2] - 1] = true;
						q.offer(new int[] { nx, ny, temp[2] - 1, temp[3] + 1 });
					}
				}
			}

			for (int i = 0; i < 4; i++) {
				int nx = temp[0] + dx[i];
				int ny = temp[1] + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny][temp[2]] && map[nx][ny] == 0) {
					visited[nx][ny][temp[2]] = true;
					q.offer(new int[] { nx, ny, temp[2], temp[3] + 1 });
				}
			}
		}

	}
}
