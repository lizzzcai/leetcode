# Bit Manipulation


## Trick

# Power of Two
```python
    is_power_of_two = num & (num-1) == 0
    # count of 1 bit is 1
    num > 0 and bin(num).count("1") == 1

```