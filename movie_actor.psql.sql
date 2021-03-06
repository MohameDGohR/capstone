PGDMP     %                     y            movie_actor    12.6    12.6                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                        0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            !           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            "           1262    32768    movie_actor    DATABASE     �   CREATE DATABASE movie_actor WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'English_United States.1252' LC_CTYPE = 'English_United States.1252';
    DROP DATABASE movie_actor;
                postgres    false            �            1259    32776    Actors    TABLE     �   CREATE TABLE public."Actors" (
    id integer NOT NULL,
    name character varying NOT NULL,
    age integer,
    gender character varying
);
    DROP TABLE public."Actors";
       public         heap    postgres    false            �            1259    32774    Actors_id_seq    SEQUENCE     �   CREATE SEQUENCE public."Actors_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public."Actors_id_seq";
       public          postgres    false    204            #           0    0    Actors_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public."Actors_id_seq" OWNED BY public."Actors".id;
          public          postgres    false    203            �            1259    32796    Movie_Actor    TABLE     X   CREATE TABLE public."Movie_Actor" (
    "Movies_id" integer,
    "Actors_id" integer
);
 !   DROP TABLE public."Movie_Actor";
       public         heap    postgres    false            �            1259    32787    Movies    TABLE     w   CREATE TABLE public."Movies" (
    id integer NOT NULL,
    title character varying NOT NULL,
    release_date date
);
    DROP TABLE public."Movies";
       public         heap    postgres    false            �            1259    32785    Movies_id_seq    SEQUENCE     �   CREATE SEQUENCE public."Movies_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public."Movies_id_seq";
       public          postgres    false    206            $           0    0    Movies_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public."Movies_id_seq" OWNED BY public."Movies".id;
          public          postgres    false    205            �            1259    32769    alembic_version    TABLE     X   CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);
 #   DROP TABLE public.alembic_version;
       public         heap    postgres    false            �
           2604    32779 	   Actors id    DEFAULT     j   ALTER TABLE ONLY public."Actors" ALTER COLUMN id SET DEFAULT nextval('public."Actors_id_seq"'::regclass);
 :   ALTER TABLE public."Actors" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    204    203    204            �
           2604    32790 	   Movies id    DEFAULT     j   ALTER TABLE ONLY public."Movies" ALTER COLUMN id SET DEFAULT nextval('public."Movies_id_seq"'::regclass);
 :   ALTER TABLE public."Movies" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    205    206    206                      0    32776    Actors 
   TABLE DATA           9   COPY public."Actors" (id, name, age, gender) FROM stdin;
    public          postgres    false    204   #                 0    32796    Movie_Actor 
   TABLE DATA           A   COPY public."Movie_Actor" ("Movies_id", "Actors_id") FROM stdin;
    public          postgres    false    207   @                 0    32787    Movies 
   TABLE DATA           ;   COPY public."Movies" (id, title, release_date) FROM stdin;
    public          postgres    false    206   ]                 0    32769    alembic_version 
   TABLE DATA           6   COPY public.alembic_version (version_num) FROM stdin;
    public          postgres    false    202   z       %           0    0    Actors_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public."Actors_id_seq"', 1, true);
          public          postgres    false    203            &           0    0    Movies_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public."Movies_id_seq"', 1, true);
          public          postgres    false    205            �
           2606    32784    Actors Actors_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."Actors"
    ADD CONSTRAINT "Actors_pkey" PRIMARY KEY (id);
 @   ALTER TABLE ONLY public."Actors" DROP CONSTRAINT "Actors_pkey";
       public            postgres    false    204            �
           2606    32795    Movies Movies_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public."Movies"
    ADD CONSTRAINT "Movies_pkey" PRIMARY KEY (id);
 @   ALTER TABLE ONLY public."Movies" DROP CONSTRAINT "Movies_pkey";
       public            postgres    false    206            �
           2606    32773 #   alembic_version alembic_version_pkc 
   CONSTRAINT     j   ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);
 M   ALTER TABLE ONLY public.alembic_version DROP CONSTRAINT alembic_version_pkc;
       public            postgres    false    202            �
           2606    32799 &   Movie_Actor Movie_Actor_Actors_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Movie_Actor"
    ADD CONSTRAINT "Movie_Actor_Actors_id_fkey" FOREIGN KEY ("Actors_id") REFERENCES public."Actors"(id);
 T   ALTER TABLE ONLY public."Movie_Actor" DROP CONSTRAINT "Movie_Actor_Actors_id_fkey";
       public          postgres    false    2708    207    204            �
           2606    32804 &   Movie_Actor Movie_Actor_Movies_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Movie_Actor"
    ADD CONSTRAINT "Movie_Actor_Movies_id_fkey" FOREIGN KEY ("Movies_id") REFERENCES public."Movies"(id);
 T   ALTER TABLE ONLY public."Movie_Actor" DROP CONSTRAINT "Movie_Actor_Movies_id_fkey";
       public          postgres    false    2710    206    207                  x������ � �            x������ � �            x������ � �            x�KJLI2�H1M65O����� 3Eu     