package baekjoon;

import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class problem2644 {
	static int N;
	static int x,y;
	static int[][] graph;
	static int cnt;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		String[] str =br.readLine().split(" ");
		x=Integer.parseInt(str[0]);
		y = Integer.parseInt(str[1]);
		int X = Integer.parseInt(br.readLine());
		graph= new int[N+1][N+1];
		for(int i=0; i<X; i++) {
			str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			graph[a][b] = graph[b][a] = 1;
		}
		boolean[] visited = new boolean[N+1];
		boolean flag= BFS(x,visited);
		if(flag) {
			System.out.println(cnt);
		}else {
			System.out.println(-1);
		}
	}
	
	static boolean BFS(int v,boolean[] visited) {
		Queue<Integer> q = new LinkedList<Integer>();
		
		q.offer(v);
		visited[v]=true;
		while(!q.isEmpty()) {
			int size = q.size();
			for(int j=0; j<size; j++) {
				int a = q.poll();
				if(a==y) {
					return true;
				}
				for(int i=1; i<=N; i++) {
					if(!visited[i] && graph[a][i] ==1) {
						visited[i]=true;
						q.offer(i);
					}
				}
			}
			cnt++;
		}
		
		return false;
	}

}
