package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class problem1008 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		StringTokenizer st= new StringTokenizer(str);
		
		double a=Integer.parseInt(st.nextToken());
		double b=Integer.parseInt(st.nextToken());
		System.out.println(a/b);
	}

}
