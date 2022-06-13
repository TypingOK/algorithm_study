package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class problem16234 {
	static int dx[] = {-1,1,0,0};
	static int dy[] = {0,0,-1,1};
	static int map[][];
	static boolean copy[][];
	static boolean visit[][];
	static int N;
	static int R;
	static int L;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		N = Integer.parseInt(str[0]);
		L = Integer.parseInt(str[1]);
		R = Integer.parseInt(str[2]);
		map = new int[N][N];
		for(int i=0; i<N; i++) {
			str = br.readLine().split(" ");
			for(int j=0; j<N; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}
		
		int answer = 0;
		
		while(true) {
			boolean flag = false;
			visit = new boolean[N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					if(BFS(i,j)) {
						flag = true;
					}
				}
			}
			if(!flag) {
				break;
			}
			answer++;
		}
		
		System.out.println(answer);
				
		
	}
	
	static boolean BFS(int x,int y) {
		Queue<int []> q = new LinkedList<int[]>();
		q.add(new int[] {x,y});
		ArrayList<int[]> list = new ArrayList<>();
		int sum =0;
		while(!q.isEmpty()) {
			int[] temp = q.poll();
			if(visit[temp[0]][temp[1]]) {
				continue;
			}
			else {
				visit[temp[0]][temp[1]] = true;
				list.add(new int[] {temp[0],temp[1]});
				sum+=map[temp[0]][temp[1]];
			}
			for(int i=0; i<4; i++) {
				int nx = temp[0] + dx[i];
				int ny = temp[1] + dy[i];
				if(0<=nx && nx<N && 0<=ny && ny<N && !visit[nx][ny]) {
					int sub = Math.abs(map[temp[0]][temp[1]]-map[nx][ny]);
					if(L<=sub && R>=sub) {
						q.add(new int[] {nx,ny});
					}
				}
			}
		}
		
		int size = list.size();
		if(size<=1) {
			return false;
		}else {
			sum = sum/list.size();
			for(int i=0; i<size; i++) {
				int temp[] = list.get(i);
				map[temp[0]][temp[1]] = sum;
			}
		}
		return true;
	}
}
