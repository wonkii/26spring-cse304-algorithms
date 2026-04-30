#include <iostream>
#include <vector>

int singleNumber(std::vector<int>& nums)
{
    int count = 0;
    int len = nums.size();

    for(int i = 0; i < len; i++){

        for(auto& ans : nums){
            if(ans == nums[i])
                count++;
        }
        if(count == 1)
            return nums[i];
        count = 0;
    }
}

int main()
{
    std::vector<int> MyVec1 = {2, 2, 1};
    std::vector<int> MyVec2 = {4, 1, 2, 2, 1};
    std::vector<int> MyVec3 = {1};
    std::cout << singleNumber(MyVec1);
    std::cout << singleNumber(MyVec2);
    std::cout << singleNumber(MyVec3);
}
