package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class problem1647_Prim {
	static class Node implements Comparable<Node>{
		int to;
		int weight;
		Node(int to, int weight){
			this.to=to;
			this.weight=weight;
		}
		public int compareTo(Node o2) {
			return this.weight-o2.weight;
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str= br.readLine().split(" ");
		int N=Integer.parseInt(str[0]);
		int M = Integer.parseInt(str[1]);
		ArrayList<Node>[] list = new ArrayList[N+1];
		for(int i=1; i<N+1; i++) {
			list[i] = new ArrayList<>();
		}
		for(int i=0; i<M; i++) {
			str = br.readLine().split(" ");
			int from = Integer.parseInt(str[0]);
			int to = Integer.parseInt(str[1]);
			int weight = Integer.parseInt(str[2]);
			list[from].add(new Node(to,weight));
			list[to].add(new Node(from,weight));
		}
		boolean visited[] = new boolean[N+1];
		PriorityQueue<Node> q = new PriorityQueue<>();
		int[] dist = new int[N+1];
		Arrays.fill(dist, Integer.MAX_VALUE);
		q.offer(new Node(1,0));
		dist[1] =0;
		int result=0;
		int max_val = Integer.MIN_VALUE;
		int cnt=0;
		while(true) {
			Node current = q.poll();
			if(visited[current.to]) {
				continue;
			}
			visited[current.to]=true;
			result+= current.weight;
			max_val = Math.max(max_val, current.weight);
			cnt++;
			if(cnt==N) break;
			int size = list[current.to].size();
			for(int i=0; i<size; i++) {
				Node n = list[current.to].get(i);
				if(!visited[n.to]) {
					q.offer(new Node(n.to,n.weight));
				}
				
			}
		}
		System.out.println(result-max_val);
	}

}
