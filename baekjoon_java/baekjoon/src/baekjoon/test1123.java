package baekjoon;

import java.text.SimpleDateFormat;
import java.util.Date;

public class test1123 {

	public static void main(String[] args) {
		Date today = new Date();
		SimpleDateFormat date = new SimpleDateFormat("yyyy/MM/dd");
		
		String[] test = date.format(today).split("/");
		
		String word = test[0]+test[1];
		
		
		System.out.println(word);
	}

}
