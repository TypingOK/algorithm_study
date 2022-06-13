package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class problem14501 {
	public static class work implements Comparable<work>{
		int start;
		int end;
		int value;
		work(int start, int doing, int value){
			this.start = start;
			this.end = start+doing-1;
			this.value=value;
		}
		@Override
		public int compareTo(work o) {
			return this.end-o.end;
		}

	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		work[] w = new work[N];
		
		for(int i=0; i<N; i++) {
			String[] str = br.readLine().split(" ");
			int a=Integer.parseInt(str[0]);
			int b=Integer.parseInt(str[1]);
			w[i] = new work(i+1,a,b);
		}
		for(int i=0; i<N; i++) {
			System.out.println(w[i].start+" "+w[i].end+" "+w[i].value);
		}
		System.out.println("-------------------------------------------");
		Arrays.sort(w);
		for(int i=0; i<N; i++) {
			System.out.println(w[i].start+" "+w[i].end+" "+w[i].value);
		}
		int MAX = Integer.MIN_VALUE;
		for(int i=0; i<N; i++) {
			int index=i;
			int sum=w[index].value;
			if(w[i].end<=N) {
				for(int j=i; j<N; j++) {
					if(w[j].end <=N && w[index].end<w[j].start) {
						sum+=w[j].value;
						index=j;
					}
				}
				MAX = Math.max(sum,MAX);
			}
		}
		System.out.println(MAX);
	}

}
