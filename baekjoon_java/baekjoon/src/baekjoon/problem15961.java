package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class problem15961 {

	public static void main(String[] args) throws IOException{
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		
		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int N =Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int[] visit = new int[d+1];
		int[] bob = new int[N+k];
		for(int i=0; i<N; i++) {
			bob[i] = Integer.parseInt(br.readLine());
		}
		for(int i=N; i<N+k; i++) {
			bob[i]=bob[i-N];
		}
		int max = Integer.MIN_VALUE;
		boolean flag = false;
		int len = 0;
		for(int i=0; i<k; i++) {
			visit[bob[i]]++;
			if(visit[bob[i]]==1) {
				len++;
			}
			if(bob[i]==c) {
				flag= true;
			}
		}
		for(int i=k; i<N+k; i++) {
			int start = i-k;
			int end = i;
			visit[bob[start]]--;
			if(visit[bob[start]]==0) {
				len--;
			}
			visit[bob[end]]++;
			if(visit[bob[end]]==1) {
				len++;
			}
			if(visit[c]>=1) {
				flag=true;
			}else {
				flag=false;
			}
			if(flag) {
				max = Math.max(max, len);
			}else {
				max = Math.max(max, len+1);
			}
		}
		System.out.println(max);
	}

}
