package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class problem11286 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		PriorityQueue<Integer> q = new PriorityQueue<>(new Comparator<Integer>() {

			@Override
			public int compare(Integer o1, Integer o2) {
				int a = Math.abs(o1);
				int b = Math.abs(o2);
				if(a==b) {
					return o1-o2;
				}
				return a-b;
			}
		});
		
		
		for(int i=0; i<n; i++) {
			int a = Integer.parseInt(br.readLine());
			if(a == 0) {
				if(q.isEmpty()) {
					System.out.println("0");
				}else {
					System.out.println(q.poll());
				}
			}else {
				q.add(a);
			}
		}
	}

}
