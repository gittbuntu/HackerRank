PGDMP         #                |            employee_timing_data    14.9    14.9     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    165879    employee_timing_data    DATABASE     x   CREATE DATABASE employee_timing_data WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
 $   DROP DATABASE employee_timing_data;
                postgres    false            �            1259    165881    employee_records    TABLE     �   CREATE TABLE public.employee_records (
    name text,
    time_in text,
    time_out text,
    reason text,
    time_difference text,
    date date
);
 $   DROP TABLE public.employee_records;
       public         heap    employeetiming    false            �          0    165881    employee_records 
   TABLE DATA           b   COPY public.employee_records (name, time_in, time_out, reason, time_difference, date) FROM stdin;
    public          employeetiming    false    209   �       �   �  x�͔�n� Ư�)� �(�z�����mmZ]�K�=�������͒�D����||�۠�藴ݙ����1Dh�1�V��k�	��cM�����ӋC�d!��Âjв-UuFT?�z9���D<�~د�AW X���4E�iC�*��.��RpG�E��d�e�Ⱥ�����_aR3> ��4p@�Z����"d�WXy � $�gȌ���MJ�2ԟ!q 9��	��&�dc��=dw�Q ����YRw�c����ڋ?��.g֊��*Kc&7��"��4S���� �1��c�h���j��<6�UE�Б��]�����t����GE�w�~���rPuT��mEԌ`ֽ��6
�P#mu\�ݞjcldk��*BH1͖8]��_��)I�d�w�˦.4X2g��hN7��\G���$��o��     