import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Scanner;

public class Main {
	
	public static String bit_to_string(boolean[] bits){
		StringBuilder sb = new StringBuilder();
		
		boolean first = true;
		for(int i = bits.length - 1; i >= 0; i--){
			if(first){
				if(bits[i]){
					first = false;
					sb.append("1");
				}
			}else{
				sb.append(bits[i] ? "1" : "0");
			}
		}
		
		if(first){
			sb.append("0");
		}
		
		return sb.toString();
	}
	
	public static boolean[] expand(char[] input){
		boolean[] bits = new boolean[32];
		
		for(int i = 0; i < 8; i++){
			final int pos = 32 - 4 * (i + 1);
			
			switch(input[i]){
			case '0':
				break;
			case '1':
				bits[pos] = true;
				break;
			case '2':
				bits[pos+1] = true;
				break;
			case '3':
				bits[pos] = true;
				bits[pos+1] = true;
				break;
			case '4':
				bits[pos+2] = true;
				break;
			case '5':
				bits[pos] = true;
				bits[pos+2] = true;
				break;
			case '6':
				bits[pos+1] = true;
				bits[pos+2] = true;
				break;
			case '7':
				bits[pos] = true;
				bits[pos+1] = true;
				bits[pos+2] = true;
				break;
			case '8':
				bits[pos+3] = true;
				break;
			case '9':
				bits[pos] = true;
				bits[pos+3] = true;
				break;
			case 'a':
				bits[pos+1] = true;
				bits[pos+3] = true;
				break;
			case 'b':
				bits[pos] = true;
				bits[pos+1] = true;
				bits[pos+3] = true;
				break;
			case 'c':
				bits[pos+2] = true;
				bits[pos+3] = true;
				break;
			case 'd':
				bits[pos] = true;
				bits[pos+2] = true;
				bits[pos+3] = true;
				break;
			case 'e':
				bits[pos+1] = true;
				bits[pos+2] = true;
				bits[pos+3] = true;
				break;
			case 'f':
				bits[pos] = true;
				bits[pos+1] = true;
				bits[pos+2] = true;
				bits[pos+3] = true;
				break;
			}
		}
		
		return bits;
	}
	
	public static String decode(boolean[] bits){
		int sum = 0;
		for(int i = 7; i < 31; i++){
			final int b = i - 7;
			sum += (bits[i] ? 1 : 0) << b;
		}
		
		int dot = 0;
		int[] array = new int[]{
				5000000, 2500000, 1250000, 625000, 312500, 156250, 78125
		};
		
		for(int i = 6; i >= 0; i--){
			final int b = 6 - i;
			dot += bits[i] ? array[b] : 0;
		}
		
		String dot_s = String.format("%07d", dot);
		int end_pos = dot_s.length();
		for(int i = 6; i >= 0; i--){
			if(dot_s.charAt(i) == '0'){
				end_pos--;
			}else{
				break;
			}
		}
		
		return ((bits[31] ? "-" : "") + sum + "." + (dot == 0 ? "0" : dot_s.substring(0, end_pos)));
	}
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		
		final int Q = sc.nextInt();
		
		for(int tt = 0; tt < Q; tt++){
			char[] input = sc.next().toCharArray();
			
			System.out.println(decode(expand(input)));
		}
		
		/*
		for(long i = 0; i < 1L << 32; i++){
			System.out.println(decode(expand(String.format("%08x", i).toCharArray())));
			
			if(!Long.toBinaryString(i).equals(bit_to_string(expand(String.format("%08x", i).toCharArray())))){
				System.out.println(i + " " + Long.toBinaryString(i) + " " + bit_to_string(expand(String.format("%08x", i).toCharArray())));
			}
		}
		*/
	}

}