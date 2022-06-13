package baekjoon;
import java.util.*;
public class problem1094 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int count=0;
		int X = scan.nextInt();
		int stick=64;
		
		while (X>0) {
			if(stick>X) {
				stick/=2;
			}
			else {
				X-=stick;
				count++;
			}
		}
		System.out.println(count);
	}
}
