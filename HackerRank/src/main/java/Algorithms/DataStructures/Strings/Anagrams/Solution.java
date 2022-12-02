package Algorithms.DataStructures.Strings.Anagrams;

import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        // Complete the function
        // Complete the function
        if (a.length() != b.length()) {
            return false;
        }

        int MAX = 26;
        int[] freqa = new int[MAX];
        int[] freqb = new int[MAX];
        for (int index = 0; index < a.length(); index++) {
            freqa[Character.toLowerCase(a.charAt(index)) - 'a']++;
            freqb[Character.toLowerCase(b.charAt(index)) - 'a']++;
        }

        //System.out.println(java.util.Arrays.toString(freqa));
        //System.out.println(java.util.Arrays.toString(freqb));
        for( int i = 0; i < MAX; i ++) {
            if ( freqa[i] != freqb[i]) {
                return false;
            }
        }
        
        return true;
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();

        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}

