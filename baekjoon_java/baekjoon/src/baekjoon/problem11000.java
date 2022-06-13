package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

public class problem11000 {

	public static class Point implements Comparable<Point>{
		int start;
		int end;
		
		Point(int start,int end){
			this.start = start;
			this.end = end;
		}
		
		@Override
		public int compareTo(Point o) {
			if(this.start==o.start) {
				return this.end-o.end;
			}
			return this.start - o.start;
		}
		
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		List<Point> list = new ArrayList<Point>();
		
		int N = Integer.parseInt(br.readLine());
		
		
		
		PriorityQueue<Integer> q = new PriorityQueue<>();
		
		for(int i=0; i<N; i++) {
			String[] str = br.readLine().split(" ");
			int start = Integer.parseInt(str[0]);
			int end = Integer.parseInt(str[1]);
			
			list.add(new Point(start,end));
		}
		Collections.sort(list);
		q.add(list.get(0).end);
		
		for(int i=1; i<N; i++) {
			if(q.peek()<=list.get(i).start) {
				q.poll();
			}
			q.add(list.get(i).end);
		}
		
		System.out.println(q.size());
		
		
		
	}

}
