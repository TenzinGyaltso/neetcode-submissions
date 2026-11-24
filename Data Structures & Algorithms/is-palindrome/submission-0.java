class Solution {
    public boolean isPalindrome(String s) {
        String reversed = new StringBuilder(s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "")).reverse().toString();

        String current = new StringBuilder(s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "")).toString();


        // System.out.println(reversed);
        // System.out.println(current);


        if (current.equals(reversed)) {
            return true;
        }
        else {
            return false;
        }

    }
}
