package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class problem1263 {

	static class Vertex implements Comparable<Vertex>{
		int no;
		int minDistance;
		
		Vertex(int no, int minDistance){
			this.no = no;
			this.minDistance = minDistance;
		}
		@Override
		public int compareTo(Vertex o) {
			return this.minDistance - o.minDistance;
		}
		
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int TC = Integer.parseInt(br.readLine());
		StringTokenizer str;
		for(int tc=1; tc<=TC; tc++) {
			str = new StringTokenizer(br.readLine(), " ");
			int N = Integer.parseInt(str.nextToken());
			
			int[][] map = new int[N][N];
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					map[i][j] = Integer.parseInt(str.nextToken());
				}
			}
			
			int min = Integer.MAX_VALUE;
			
			for(int i=0; i<N; i++) {
				int sum =0;
				int[] distance = new int[N];
				boolean[] visited = new boolean[N];
				
				PriorityQueue<Vertex> pq = new PriorityQueue<>();
				
				Arrays.fill(distance, Integer.MAX_VALUE);
				distance[i] = 0;
				pq.offer(new Vertex(i,distance[i]));
				
				while(!pq.isEmpty()) {
					Vertex current = pq.poll();
					
					if(visited[current.no]) {
						continue;
					}
					visited[current.no] = true;
					
					for(int j=0; j<N; j++) {
						if(!visited[j] && map[current.no][j] != 0 && distance[j]> map[current.no][j]+distance[current.no]) {
							distance[j] =distance[current.no]+map[current.no][j];
							pq.offer(new Vertex(j,distance[j]));
						}
					}
				}
				
				for(int j=0; j<N; j++) {
//					System.out.println(distance[j]);
					sum+=distance[j];
				}
				if(sum<min) {
					min = sum;
				}
				
			}
			
			System.out.println("#"+tc+" "+min);
			
		}
	}

}
