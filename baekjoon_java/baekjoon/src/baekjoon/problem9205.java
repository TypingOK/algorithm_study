package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem9205 {

	public static class Point {
		int x;
		int y;
		Point(int x, int y){
			this.x=x;
			this.y=y;
		}
	}
	static int N;
	static boolean[] visited;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		for(int tc=0; tc<t; tc++) {
			int p = Integer.parseInt(br.readLine());
			Point[] point = new Point[p+2];
			visited = new boolean[p+2];
			String[] str= br.readLine().split(" ");
			point[0] = new Point(Integer.parseInt(str[0]),Integer.parseInt(str[1]));
			for(int i=1; i<p+1; i++) {
				str=br.readLine().split(" ");
				point[i] = new Point(Integer.parseInt(str[0]),Integer.parseInt(str[1]));
			}
			str = br.readLine().split(" ");
			point[p+1] = new Point(Integer.parseInt(str[0]),Integer.parseInt(str[1]));
			BFS(point);
		}
		
	}
	
	static void BFS(Point[] point) {
		Queue<Point> q = new LinkedList<>();
		q.offer(point[0]);
		visited[0]=true;
		int size = point.length-1;
		while(!q.isEmpty()) {
			Point l = q.poll();
			int x = l.x;
			int y = l.y;
			if(Math.abs(point[size].x-x)+ Math.abs(point[size].y-y)<=1000) {
				System.out.println("happy");
				return;
			}
			for(int i=1; i<size; i++) {
				if(!visited[i]) {
					int dist = Math.abs(point[i].x-x)+ Math.abs(point[i].y-y);
					if(dist<=1000) {
						visited[i]=true;
						q.offer(point[i]);
					}
				}
			}
		}
		System.out.println("sad");
		return;
	}
}
