# 1. Major Entity

## 1.1. Module

### 1.1.1. port

port describe the input/output interface of the module. The clk and rst_n are provided in default with following declaration:

```c++
    sc_core::sc_in_clk clk;
    sc_core::sc_in<bool> rst_n;
```

you may override the clk and rst_n in the module declaration, however, in such case, you need mannually connect them with correct signals.

The full port declartion as following:

```c++
port:
  - read_in : 
      kind : PORT/in/out   // PORT as default
      message : <defined-in-message>
```

In default, if you only name the port without any other detailed description, the port will be considered as one in-out-port(PORT) with fifo as connnected signal.


## 1.2. Message

Message(struct) will be auto-genreated based on 'connection' defined in module by connecting two ports name :

```
  WARP_SCHEDULER.FETCH : FETCH.WARP_SCHEDULER  -> if_WARP_SCHEDULER_FETCH__FETCH_WARP_SCHEDULER
```

All messages will be generated into 'interface_def.h' file

## 1.3. Register


# 2. Detailed Unit

## 2.1. LUT-GEMM Unit

LUT Unit contains
- LUT Dispatch
- LUTGenArray : LUTGens in same array share value bus
  - LUTGen x 4 per array
- LUTAccArray : LUTAccs in same array share value bus
  - LUTAcc x 4 per array

Key configurations:
- instruction tile size(MNK): we suppose the size is 16 * 8 * 16
  - Reference CUDA Tensor Core size : 16 * 8 * 16

Target execution expression as :

```
D = A * B + C
```

Matrix element type format should be [mx-format](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf)

Reference: https://zhuanlan.zhihu.com/p/1932073634538694566

Here maps as"
- w = B
- x = A

the LUT-GEMM requires two steps:
1. 