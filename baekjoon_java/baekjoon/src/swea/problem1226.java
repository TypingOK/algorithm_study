package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class problem1226 {

	static int N = 16;
	static int[][] map;
	static boolean visit[][];
	static int[] dx = {1,0,-1,0};
	static int[] dy = {0,1,0,-1};
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		for (int tc = 1; tc <= 10; tc++) {
			visit = new boolean[N][N];
			map = new int[N][N];
			String pppppp = br.readLine();
			char[] str;
			int[] start = new int[2];
			for(int i=0; i<N; i++) {
				str = br.readLine().toCharArray();
				for(int j=0; j<N; j++) {
					map[i][j] = (int)str[j]-'0';
					if(map[i][j] == 2) {
						start[0] = i;
						start[1] = j;
					}
				}
			}
			boolean flag=bfs(start[0],start[1]);
			if(flag) {
				System.out.println("#"+tc+" "+1);
			}else {
				System.out.println("#"+tc+" "+0);
			}
			
			
		}
		
		
	}
	
	static boolean bfs(int x, int y) {
		Queue<int[]> q = new LinkedList<int[]>();
		q.add(new int[] { x, y });
		visit[x][y] = true;

		while (!q.isEmpty()) {
			int[] temp = q.poll();
			if(map[temp[0]][temp[1]] == 3) {
				return true;
			}
			for (int i = 0; i < 4; i++) {
				int nx = temp[0] + dx[i];
				int ny = temp[1] + dy[i];
				if (0 <= nx && nx < N && 0 <= ny && ny < N &&map[nx][ny]!=1 && !visit[nx][ny]) {
					visit[nx][ny] = true;
					q.add(new int[] {nx,ny});
				}
			}
		}
		return false;
	}

}
