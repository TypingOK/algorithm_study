package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class problem1297  {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int d = Integer.parseInt(str[0]);
		int h = Integer.parseInt(str[1]);
		int w= Integer.parseInt(str[2]);
		
		double res= Math.sqrt(Math.pow(d,2)/(Math.pow(h, 2)+Math.pow(w, 2)));
		System.out.print((int)Math.floor(res*h)+" ");
		System.out.println((int)Math.floor(res*w));
		
	}

}
