--Załóż bazę danych, która będzie zawierać dane ogłoszeń, analogiczne do tych w utworzonych wcześniej klasach.

--Wersja prostsza: stwórz jedną tabelę dla ogłoszeń samochodowych (zarówno dane ogólne, jak i dane samochodu).
--Zadbaj o odpowiednie typy kolumn (szczególnie ważne dla „prawdziwych” baz danych).

--Wersja bardziej złożona: trzymaj dane sprzedawców w oddzielnej tabeli, a w ogłoszeniach odwołuj się do sprzedawców za pomocą `id` ("klucz obcy") tak,
--aby ten sam sprzedawca mógł mieć przypisanych wiele ogłoszeń.

--Wersja jeszcze bardziej złożona (tylko dla tych, którzy już znają bazy danych): ogólne dane ogłoszeń trzymaj w jednej tabeli,
--a rozszerzone dane dotyczące samochodów w oddzielnej. Wówczas można też dodać tabelę zawierającą rozszerzone dane dla ogłoszeń mieszkaniowych.

--Wypełnij tabelę (/tabele) przykładowymi danymi.


CREATE SEQUENCE annoncement_anoncementID_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE SEQUENCE  seller_sellerID_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

CREATE TABLE IF NOT EXISTS public.seller
(
    sellerID integer NOT NULL DEFAULT nextval('seller_sellerID_seq'::regclass),
    FirstName varchar ,
    LastName varchar ,
    Phone varchar,
    email varchar,
    CONSTRAINT seller_pkey PRIMARY KEY (sellerID)
)

CREATE TABLE annoncement
(
    anoncementID integer NOT NULL DEFAULT nextval('annoncement_anoncementID_seq'::regclass),
	sellerID integer NOT NULL ,
    description text,
    price float,
    subject varchar,
    CONSTRAINT annoncement_pkey PRIMARY KEY (anoncementID),
    CONSTRAINT seller_ID FOREIGN KEY (sellerID)
        REFERENCES Seller (sellerID) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE carextensions
(
    anoncementID integer NOT NULL, 
    brand varchar(32),
    model varchar(32),
    course float,
    year integer,
    colour varchar(32),
    CONSTRAINT CarExtensions_pkey PRIMARY KEY (anoncementID),
    CONSTRAINT anoncement_ID FOREIGN KEY (anoncementID)
        REFERENCES Annoncement (anoncementID) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

CREATE TABLE  propertyextensions
(
    anoncementID integer NOT NULL ,
    city varchar(32),
    area varchar(32),
    rooms integer,
    CONSTRAINT PropertyExtensions_pkey PRIMARY KEY (anoncementID),
    CONSTRAINT anoncement_ID FOREIGN KEY (anoncementID)
        REFERENCES  Annoncement (anoncementID) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
 
INSERT INTO Seller (sellerID,FirstName,LastName,Phone,email) VALUES (nextval('seller_sellerID_seq'),'Teodor','Roosvelt','+48123456789','Teodor.Roosvelt@gmail.com');
INSERT INTO Seller (sellerID,FirstName,LastName,Phone,email) VALUES (nextval('seller_sellerID_seq'),'Franklin','Roosvelt','+48123456788','Franklin.Roosvelt@gmail.com');
INSERT INTO Seller (sellerID,FirstName,LastName,Phone,email) VALUES (nextval('seller_sellerID_seq'),'Ronald','Regan','+48123456787','Ronald.Regan@gmail.com');
INSERT INTO Seller (sellerID,FirstName,LastName,Phone,email) VALUES (nextval('seller_sellerID_seq'),'Margaret','Thatcher','+48123456786','Margaret.Thatcher@gmail.com');
INSERT INTO Seller (sellerID,FirstName,LastName,Phone,email) VALUES (nextval('seller_sellerID_seq'),'Tony','Blair','+48123456785','Tony.Blair@gmail.com');

-- Teodor Roosvelt cars
do $$
declare
  seller_ID integer;
  anoncement_ID integer;
begin
 select sellerID into seller_ID  from Seller where FirstName='Teodor' and Lastname='Roosvelt';

INSERT INTO annoncement (anoncementID,sellerID,subject,description,price) VALUES 
(nextval('annoncement_anoncementid_seq'),
seller_ID,
'Sprzedam Forda model 1912','This 1912 Ford Model T is a five-passenger touring model that was refurbished during previous ownership and purchased by the seller four years ago. It is powered by a replacement 177ci four-cylinder paired with a two-speed Model T transmission and a Ruckstell axle. Finished in blue over a black buttoned-leather interior, the car is equipped with a black soft top, a Laycock overdrive unit, rear disc brakes, and turn signals. This Model T has been used on multiple tours and is now offered with a spare engine and rear axle, other spare parts, custom side curtains, a set of fore doors, and a clean Virginia title in the seller’s name.',
223031
);
select anoncementID into anoncement_ID from annoncement where sellerID=seller_ID and subject='Sprzedam Forda model 1912';
insert into carextensions (anoncementID, brand, model, course, year, colour ) values (anoncement_ID, 'Ford', 'm 1912', 45000, 1915, 'black' );

INSERT INTO annoncement (anoncementID,sellerID,subject,description,price) VALUES 
(nextval('annoncement_anoncementid_seq'),
seller_ID,
'Sprzedam Forda model A','Pojazd ten posiadał znacznie nowocześniejsze rozwiązania techniczne niż Ford T i stał się w USA jednym z najpopularniejszych samochodów końca lat dwudziestych i początku lat trzydziestych XX wieku. Był drugim w historii fabryki samochodem marki Ford w którego nazwie wykorzystano pierwszą literę alfabetu. Samochód pod takim samym oznaczeniem produkowano w zakładach Forda także w latach 1903–1904. Ford Model A z roku 1903 był pierwszym modelem samochodu jaki produkował Ford.',
123030);
 
select anoncementID into anoncement_ID from annoncement where sellerID=seller_ID and subject='Sprzedam Forda model A';
insert into carextensions (anoncementID, brand, model, course, year, colour ) values (anoncement_ID, 'Ford', 'm A 1927', 47000, 1930, 'black' );

end; $$

-- Eleonora Roosvelt cars
do $$
declare
  seller_ID integer;
  anoncement_ID integer;
begin
 select sellerID into seller_ID  from Seller where FirstName='Eleonora' and Lastname='Roosvelt';

INSERT INTO annoncement (anoncementID,sellerID,subject,description,price) VALUES 
(nextval('annoncement_anoncementid_seq'),
seller_ID,
'Sprzedam Forda model 1912r','This 1912 Ford Model T is a five-passenger touring model that was refurbished during previous ownership and purchased by the seller four years ago. It is powered by a replacement 177ci four-cylinder paired with a two-speed Model T transmission and a Ruckstell axle. Finished in blue over a black buttoned-leather interior, the car is equipped with a black soft top, a Laycock overdrive unit, rear disc brakes, and turn signals. This Model T has been used on multiple tours and is now offered with a spare engine and rear axle, other spare parts, custom side curtains, a set of fore doors, and a clean Virginia title in the seller’s name.',
223031
);
select anoncementID into anoncement_ID from annoncement where sellerID=seller_ID and subject='Sprzedam Forda model 1912r';
insert into carextensions (anoncementID, brand, model, course, year, colour ) values (anoncement_ID, 'Ford', 'm 1912', 25000, 1917, 'black' );

INSERT INTO annoncement (anoncementID,sellerID,subject,description,price) VALUES 
(nextval('annoncement_anoncementid_seq'),
seller_ID,
'Sprzedam Forda model T','Samochód Ford Model T powstał w 1908 roku. Jego głównymi konstruktorami byli: Henry Ford, C. Harold Wills, József Galamb i Jenő Farkas. Głównym założeniem Henry ego Forda było stworzenie samochodu dla przeciętnej amerykańskiej rodziny. Dodatkowo auto miało być tanie, o prostej budowie, łatwe w naprawie, proste w prowadzeniu, mieć miękkie zawieszenie i duży prześwit, umożliwiający jazdę po bezdrożach. Koncepcja okazała się trafiona. 27 września 1908 roku bramy fabryki Piquette Plant w Detroit opuścił pierwszy egzemplarz Forda T. Datę tę uznaje się za początek masowej motoryzacji.',
145030);
 
select anoncementID into anoncement_ID from annoncement where sellerID=seller_ID and subject='Sprzedam Forda model T';
insert into carextensions (anoncementID, brand, model, course, year, colour ) values (anoncement_ID, 'Ford', 'm T 1908', 37000, 1925, 'black' );

end; $$


-- Ronald Regan rancho
do $$
declare
  seller_ID integer;
  anoncement_ID integer;
begin
 select sellerID into seller_ID  from Seller where FirstName='Ronald' and Lastname='Regan';

INSERT INTO annoncement (anoncementID,sellerID,subject,description,price) VALUES 
(nextval('annoncement_anoncementid_seq'),
seller_ID,
'Sprzedam Rancho del Cielo','The ranch was originally named Rancho de los Picos after José Jesús Pico—a descendant of Santiago de la Cruz Pico who arrived with the Anza expedition in 1776—who homesteaded it and built the original adobe house in 1871. The Pico family owned the ranch until 1941, when Joe, one of Jose Picos sons, sold it to Frank Flournoy, a Santa Barbara County surveyor',
2527000
);
select anoncementID into anoncement_ID from annoncement where sellerID=seller_ID and subject='Sprzedam Rancho del Cielo';
insert into propertyextensions (anoncementID, city, area, rooms  ) values (anoncement_ID, 'Santa Barbara,', '439', 5  );

INSERT INTO annoncement (anoncementID,sellerID,subject,description,price) VALUES 
(nextval('annoncement_anoncementid_seq'),
seller_ID,
'Sprzedam Bel Air','The longtime Bel-Air home of former president Ronald Reagan and his wife, Nancy, has sold for $15 million in an off-market deal. The buyer is Jerry Perenchio, the billionaire businessman and former chairman of Univision, according to records obtained by The Times.',
15000000);
 
select anoncementID into anoncement_ID from annoncement where sellerID=seller_ID and subject='Sprzedam Bel Air';
insert into propertyextensions (anoncementID, city, area, rooms  ) values (anoncement_ID, 'Los Angeles,', '1439', 15  );

end; $$


-- Margaret Thatcher apartment
do $$
declare
  seller_ID integer;
  anoncement_ID integer;
begin
 select sellerID into seller_ID  from Seller where FirstName='Ronald' and Lastname='Regan';

INSERT INTO annoncement (anoncementID,sellerID,subject,description,price) VALUES 
(nextval('annoncement_anoncementid_seq'),
seller_ID,
'Sprzedam mieszkanie w Londynie','Located at 112 Swan Court, just off the Kings Road, the 1,173-square-foot sixth-floor apartment was the home of Margaret and Denis Thatcher after they married in December 1951, according to letting agents Strutt & Parker.',
1200000
);
select anoncementID into anoncement_ID from annoncement where sellerID=seller_ID and subject='Sprzedam mieszkanie w Londynie';
insert into propertyextensions (anoncementID, city, area, rooms  ) values (anoncement_ID, 'London', '439', 5  );

INSERT INTO annoncement (anoncementID,sellerID,subject,description,price) VALUES 
(nextval('annoncement_anoncementid_seq'),
seller_ID,
'Sprzedam dom M Thatcher','Margaret Thatcher’s London home, where the onetime prime minister of the U.K. lived from 1991 until her passing in 2013, is an elegant piece of history in the heart of the city’s Belgravia district. Although newly refurbished, the Georgian-style house retains much of its 19th-century detailing. Behind the handsome stucco façade, which includes a steel-lined bombproof door, the entrance hall features Hopton Wood flooring, the same type used in the Houses of Parliament. There’s also a formal dining room linked to a study',
41000000);
 
select anoncementID into anoncement_ID from annoncement where sellerID=seller_ID and subject='Sprzedam dom M Thatcher';
insert into propertyextensions (anoncementID, city, area, rooms  ) values (anoncement_ID, 'London', '539', 13  );

end; $$
