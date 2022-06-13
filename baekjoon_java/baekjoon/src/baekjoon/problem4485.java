package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class problem4485 {
	
	static int dx[] = {1,0,-1,0};
	static int dy[] = {0,1,0,-1};
	static int N;
	static int[][] map;
	static int ans;
	static boolean visited[][];
	static int [][] copy;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc=0;
		String str[];
		while(true) {
			N = Integer.parseInt(br.readLine());
			if (N == 0) {
				break;
			}
			tc++;
			ans =Integer.MAX_VALUE;
			visited = new boolean[N][N];
			copy = new int[N][N];
			map = new int[N][N];
			for(int i=0; i<N; i++) {
				str = br.readLine().split(" ");
				for(int j=0; j<N; j++) {
					map[i][j] = Integer.parseInt(str[j]);
					copy[i][j] = Integer.MAX_VALUE;
				}
			}
			copy[0][0] = map[0][0];
//			DFS(0,0,map[0][0]);
			BFS();
			System.out.println("Problem "+tc+": "+ans);
		}
		
	}
	static void DFS(int x,int y, int count) {
		visited[x][y] = true;
		if(count>=ans) {
			return;
		}
		if(x==N-1 && y==N-1) {
			ans = Math.min(count,ans);
			return;
		}
		for(int i=0; i<4; i++) {
			int nx= x+dx[i];
			int ny = y+dy[i];
			if(0<=nx && nx<N && 0<= ny && ny<N && !visited[nx][ny] &&count+map[nx][ny]<copy[nx][ny]) {
				copy[nx][ny] = count+map[nx][ny];
				DFS(nx,ny,count+map[nx][ny]);
				visited[nx][ny] = false;
			}
		}
	}
	
	static void BFS() {
		PriorityQueue<Node> q = new PriorityQueue<>();
		q.add(new Node(map[0][0],0,0));
		copy[0][0] = map[0][0];
		
		while(!q.isEmpty()) {
			Node temp = q.poll();
			int x = temp.x;
			int y = temp.y;
			int price = temp.price;
	
			if(x==N-1 && y == N-1) {
				ans = price;
				break;
			}
			for(int i=0; i<4; i++) {
				int nx = x+dx[i];
				int ny = y+dy[i];
				if(0<=nx && nx<N && 0<=ny && ny<N && !visited[nx][ny] &&price +map[nx][ny]<copy[nx][ny]) {
					visited[nx][ny] = true;
					copy[nx][ny] = price+map[nx][ny];
					q.offer(new Node(copy[nx][ny],nx,ny));
				}
			}
		}
		
		
	}
	static public class Node implements Comparable<Node>{
		int x;
		int y;
		int price;
		Node(int price,int x,int y){
			this.price = price;
			this.x = x;
			this.y = y;
		}
		@Override
		public int compareTo(Node o) {
			return this.price - o.price;
		}
	}
}
