PGDMP                      }            triage_system_db    17.4    17.4     )           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            *           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            +           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            ,           1262    24597    triage_system_db    DATABASE     v   CREATE DATABASE triage_system_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en-US';
     DROP DATABASE triage_system_db;
                     postgres    false            -           0    0    DATABASE triage_system_db    ACL     8   GRANT ALL ON DATABASE triage_system_db TO triage_admin;
                        postgres    false    4908            �            1259    24600    patients    TABLE     �  CREATE TABLE public.patients (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    age integer NOT NULL,
    gender character varying(20),
    weight double precision NOT NULL,
    heart_rate integer,
    blood_pressure integer,
    temperature numeric(4,1),
    chief_complaint_chest_pain boolean DEFAULT false,
    chief_complaint_fever boolean DEFAULT false,
    chief_complaint_headache boolean DEFAULT false,
    chief_complaint_difficulty_breathing boolean DEFAULT false,
    chief_complaint_abdominal_pain boolean DEFAULT false,
    chief_complaint_fracture boolean DEFAULT false,
    chief_complaint_unconscious boolean DEFAULT false,
    chief_complaint_nausea boolean DEFAULT false,
    chief_complaint_stroke_symptoms boolean DEFAULT false,
    chief_complaint_burn_injury boolean DEFAULT false,
    severity character varying(50) DEFAULT 'Unknown'::character varying
);
    DROP TABLE public.patients;
       public         heap r       postgres    false            .           0    0    TABLE patients    ACL     4   GRANT ALL ON TABLE public.patients TO triage_admin;
          public               postgres    false    218            �            1259    24599    patients_id_seq    SEQUENCE     �   CREATE SEQUENCE public.patients_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.patients_id_seq;
       public               postgres    false    218            /           0    0    patients_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.patients_id_seq OWNED BY public.patients.id;
          public               postgres    false    217            0           0    0    SEQUENCE patients_id_seq    ACL     G   GRANT SELECT,USAGE ON SEQUENCE public.patients_id_seq TO triage_admin;
          public               postgres    false    217            �           2604    24603    patients id    DEFAULT     j   ALTER TABLE ONLY public.patients ALTER COLUMN id SET DEFAULT nextval('public.patients_id_seq'::regclass);
 :   ALTER TABLE public.patients ALTER COLUMN id DROP DEFAULT;
       public               postgres    false    218    217    218            &          0    24600    patients 
   TABLE DATA           �  COPY public.patients (id, name, age, gender, weight, heart_rate, blood_pressure, temperature, chief_complaint_chest_pain, chief_complaint_fever, chief_complaint_headache, chief_complaint_difficulty_breathing, chief_complaint_abdominal_pain, chief_complaint_fracture, chief_complaint_unconscious, chief_complaint_nausea, chief_complaint_stroke_symptoms, chief_complaint_burn_injury, severity) FROM stdin;
    public               postgres    false    218   �       1           0    0    patients_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.patients_id_seq', 1, false);
          public               postgres    false    217            �           2606    24616    patients patients_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.patients DROP CONSTRAINT patients_pkey;
       public                 postgres    false    218            &      x������ � �     