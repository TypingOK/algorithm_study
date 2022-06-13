package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class problem17471 {
	
	static int N;
	static boolean visit[];
	static boolean [][] adj;
	static int answer;
	
	static int[] people;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		String str[] = br.readLine().split(" ");
		
		people = new int[N+1];
		for(int i=0; i<N; i++) {
			people[i+1] = Integer.parseInt(str[i]);
		}
		adj = new boolean[N+1][N+1];
		visit = new boolean[N+1];
		
		for(int i=1; i<=N; i++) {
			str=br.readLine().split(" ");
			int M = Integer.parseInt(str[0]);
			for(int j=1; j<=M; j++) {
				adj[i][Integer.parseInt(str[j])] = true; 
			}
		}
		
		
		answer = Integer.MAX_VALUE;
		powerSet(1);
		if(answer == Integer.MAX_VALUE) {
			System.out.println(-1);
		}else {
			System.out.println(answer);
		}
	}
	
	static void powerSet(int index) {
		if(index == N+1) {
			
			int countA = 0,countB = 0;
			int cntA = 0, cntB = 0;
			
			for(int i=1; i<=N; i++) {
				if(visit[i]) {
					countA = i;
					cntA++;
				}else {
					countB = i;
					cntB++;
				}
			}
			
			int peopleA = BFS(countA,cntA);
			int peopleB = BFS(countB,cntB);
			
			if(peopleA>0 && peopleB>0) {
				answer = Math.min(answer, Math.abs(peopleA-peopleB));
			}
			
			return ;
		}
		
		visit[index] = true;
		powerSet(index+1);
		visit[index] = false;
		powerSet(index+1);
	}
	
	static int BFS(int start, int count) {
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(start);
		boolean[] v = new boolean[N+1];
		v[start] = true;
		
		int peopleCnt=0, cnt = 0;
		while(!q.isEmpty()) {
			int cur = q.poll();
			cnt++;
			peopleCnt += people[cur];
			for(int i=1; i<=N; i++) {
				if(adj[cur][i] && visit[cur] == visit[i] && !v[i]) {
					q.add(i);
					v[i] = true;
				}
			}
		}
		
		if(cnt == count) {
			return peopleCnt;
		}else {
			return -1;
		}
	}

}
